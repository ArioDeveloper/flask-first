from flask import Flask , request , jsonify
from rubika.client import Bot
import requests
import os
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


@app.route('/main)
def about():
    r=requests.get("https://boiling-mountain-37861.herokuapp.com/main")
    return r.text


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


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
    
   
