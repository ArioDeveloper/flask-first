from flask import Flask , request , jsonify ,send_file
from rubika.client import Bot
import requests
import os
import io
from googlesearch import search


app = Flask(__name__)




@app.route('/')
def home():
    return '<h1><center>Home Page Route</h1></center>'


@app.route('/main')
def about():
    r=requests.get("https://boiling-mountain-37861.herokuapp.com/main")
    return r.text


@app.route('/image/<path:path>')
def image(path):
    r=requests.get(f"https://boiling-mountain-37861.herokuapp.com/image/{path}")
    file_like_object = io.BytesIO()
    file_like_object.write(r.content)
    file_like_object.seek(0)  # move to the beginning of file 

    return send_file(file_like_object, mimetype='image/png')

@app.route('/file/<path:path>')
def file(path):
    r=requests.get(f"https://boiling-mountain-37861.herokuapp.com/file/{path}")
    file_like_object = io.BytesIO()
    file_like_object.write(r.content)
    file_like_object.seek(0)  # move to the beginning of file 
    if (path.split(".")[-1] == "png" or path.split(".")[-1] == "jpg"):
        mim="image/png"
    elif (path.split(".")[-1] == "mp4"):
        mim="video/mp4"
    return send_file(file_like_object, mimetype = mim)

 


@app.route('/s' , methods=['GET'])
def search():
        q= request.args.get('q')
        r=requests.get(f"https://boiling-mountain-37861.herokuapp.com/s?q={q}")
        return r.text

@app.route('/d' , methods=['GET'])
def d():
        r=requests.get(f"https://boiling-mountain-37861.herokuapp.com/d")
        return r.text
@app.route('/q' , methods=['GET'])
def q():
        q= request.args.get('q')
        r=requests.get(f"https://boiling-mountain-37861.herokuapp.com/q?q={q}")
        return r.text


