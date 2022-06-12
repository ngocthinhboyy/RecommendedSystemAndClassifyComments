import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


sheet_id='1pDUnpfB8fdegJdKtplUi0FZFGw3EPESr9ioruAWRRew'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
df



cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["Combine"]) #feeding combined strings(mobile contents) to CountVectorizer() object




cosine_sim = cosine_similarity(count_matrix)
print(cosine_sim)



def get_title_from_index(index):
    return df[df.index == index]["Name"].values[0]
def get_index_from_title(Name):
    return df[df.Name == Name]["index"].values[0]







#mobile_user_likes = "iPhone 11"
#mobile_index = get_index_from_title(mobile_user_likes)













def top_5_similar_product(index):
    mobile_index = index
    similar_moblie = list(enumerate(cosine_sim[mobile_index])) 
    #accessing the row corresponding to given mobile to find all the similarity scores for that mobile and then enumerating over it
    print(similar_moblie)
    print("================================================")
    sorted_similar_mobile = sorted(similar_moblie,key=lambda x:x[1],reverse=True)[1:]
    print(sorted_similar_mobile)

    arr=[]
    i=0
    #print("Top 5 similar mobile to " + mobile_user_likes + " are:\n")
    print("Top 5 similar mobile to " + " are:\n")
    for element in sorted_similar_mobile:
        #print(get_title_from_index(element[0]))
        arr.append(element[0])
        i=i+1
        if i>=5:
            break
    return arr

