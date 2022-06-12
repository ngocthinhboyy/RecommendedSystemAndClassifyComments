import sklearn
import numpy as np
import pandas as pd


sheet_id_train='1dMtr4v5XvSaPd0khTK1k8ak4QgQPrwrH9KBAIPzgm_Q' 

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id_train}/export?format=csv")



#!pip install tweet-preprocessor
#import re
#REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\|)|(\()|(\))|(\[)|(\])|(\%)|(\$)|(\>)|(\<)|(\{)|(\})")
#REPLACE_WITH_SPACE = re.compile("(<br\s/><br\s/?)|(-)|(/)|(:).")

#import preprocessor as p

# custum function to clean the dataset (combining tweet_preprocessor and reguar expression)
#def clean_tweets(df):
#  tempArr = []
#  for line in df:
#    # send to tweet_processor
#    tmpL = p.clean(line)
#    # remove puctuation
#    tmpL = REPLACE_NO_SPACE.sub("", tmpL.lower()) # convert all tweets to lower cases
#    tmpL = REPLACE_WITH_SPACE.sub(" ", tmpL)
#    tempArr.append(tmpL)
#  return tempArr

# train_tweet = clean_tweets(df["comment"])
# train_tweet = pd.DataFrame(train_tweet)

# append cleaned tweets to the training data
# df["clean_content"] = train_tweet

# compare the cleaned and uncleaned tweets
# df.head(10)


df['comment'] = df['comment'].str.lower()
df
#(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\|)|(\()|(\))|(\[)|(\])|(\%)|(\$)|(\>)|(\<)|(\{)|(\})


df["clean_comment"]=df["comment"].str.replace("[.;:!'?,''@#$%^&*()]"," ")
df


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import  LinearSVC

from sklearn.multiclass import OneVsRestClassifier



tfidf=TfidfVectorizer(analyzer='word',max_features=1000)
X=tfidf.fit_transform(df['comment'].values.astype('U'))


tfidf.vocabulary_
X.shape



y = y = df.iloc[:, 2:3].values
y


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


sgd =SGDClassifier()
lr=LogisticRegression(solver='lbfgs')
svc=LinearSVC()




def j_score(y_true,y_pred):
  jaccard=np.minimum(y_true,y_pred).sum(axis=1)/np.maximum(y_true,y_pred).sum(axis=1)
  return jaccard.mean()*100


def print_score(y_pred, clf):
  #print("Clf: ", clf.__class__.__name__)
  print(' score: {}'.format(j_score(y_test,y_pred)))
  print('----')




for classifier in [svc,lr,sgd]: #for classifier in [sgd,lr,svc]:
  clf=OneVsRestClassifier(classifier)
  clf.fit(X_train,y_train)
  y_pred=clf.predict(X_test)
  #print_score(y_pred,classifier)





def print_result(sentence):
    #print('hello day la thanh')
    #print(df)

    #print('day la ket qua: ')



    x=[sentence]
    xt=tfidf.transform(x)
    clf.predict(xt)
    t=clf.predict(xt)


    #import codecs, json
    #obj_text = codecs.open(file_path, 'r', encoding='utf-8').read()
    #b_new = json.loads(obj_text)
    #a_new = np.array(b_new)

    return t






