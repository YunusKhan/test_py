import re, os, tensorflow as tf, numpy as np, pandas as pd, sklearn
import pymongo, os, flask, requests
from flask import Flask, render_template, request,json, Response
from conn import mongo_conn

app = Flask(__name__)

@app.route('/')
def signUp():
    return render_template('hello.html')

@app.route('/', methods=['POST'])
def send():
    name = request.form['text']
    conn = mongo_conn()
    result = conn.send_data(name)
    return render_template('hello.html', result = result)


if __name__=="__main__":
    app.run(debug=True)