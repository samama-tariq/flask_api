import json 
from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return "hello world"

if __name__=='__main__':
    app.run(debug=True,host='localhost',port=8080)
