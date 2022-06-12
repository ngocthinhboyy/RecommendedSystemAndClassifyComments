from flask import Flask, request, jsonify
from comment_model import print_result
from test_file_connection import my_function
from model import top_5_similar_product
from comment_model import print_result

app=Flask(__name__)

@app.route('/comment',methods=['GET','POST'])
def get_or_post():
    if request.method == "GET":
        return jsonify({"respone":"hi, thanh"})
    elif request.method =="POST":
        req_JSON=request.get_json(force = True)
        print(request.json)
        req_JSON=request.json
        print(req_JSON)
        name= req_JSON['sentences']
        sentences = []
        for a in name:
            sentences.append(a);
        results = []
        for sentence in sentences:
            result = print_result(sentence)
            results.append(str(result[0]))
        print('1 => tich cuc')
        print('0 => tieu cuc')
        new_obj={
            'results':results
        }

        

        print(new_obj)
        #return jsonify({"response": result })

        return new_obj



@app.route('/mobile',methods=['GET','POST'])
def test():
    if request.method == "GET":
        return jsonify({"respone":"hi, thanh"})
    elif request.method =="POST":
        req_JSON=request.json
        name= req_JSON['name']
        return jsonify({"response": "Hello" + name})
    

@app.route('/mobile/<int:id>',methods=['GET'])
def test1(id):
    if request.method =="GET":
        arr=top_5_similar_product(id)
        for i in arr:
            print(i)
        #print('hello------------------')
        #print(arr)
        new_obj={
            'list_result':arr
        }
        return jsonify(new_obj)

if __name__ == '__main__':
    app.run(debug=True,port=9090)

#print(name)


#pip install pandas
#pip install numpy





