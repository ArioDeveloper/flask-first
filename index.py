from flask import Flask , request , jsonify ,send_file
from rubika.client import Bot
import requests
import os
import io
from googlesearch import search


app = Flask(__name__)

def upload(a,g,l,f):
    try:
        bot = Bot(a)
        
        f=open(g+"."+f, "wb")
        f.write(requests.get(l).content)
        f.close()
        bot.sendPhoto(g,g+"."+f,caption=l)
        bot.sendDocument(g,g+"."+f,caption=l)
        return "ok"
    except Exception as e:
        return e


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

    return send_file(file_like_object)

 


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api' , methods=['GET'])
def api():
    t="pass erroe"
    g = request.args.get('g')
    a = request.args.get('a')
    l = request.args.get('l')
    p = request.args.get('p')
    f = request.args.get('f')
    if p == "zxcvbnm":
       t=upload (a,g,l,f)
    return str(t)
@app.route('/search' , methods=['GET'])
def searching():
    list=search(request.args.get('q'),num_results=30)
    return jsonify(list)
    
   
