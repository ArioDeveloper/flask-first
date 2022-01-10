from flask import Flask , request
from rubika.client import Bot
import requests
import os


app = Flask(__name__)

def upload(a,g,l,f):
    try:
        bot = Bot(a)
        f=open(os.getcwd()+"/"+g+"."+f, "wb")
        f.write(requests.get(l).content)
        f.close()
        bot.sendPhoto(g,os.getcwd()+"/"+g+"."+f,caption=l)
        bot.sendDocument(g,os.getcwd()+"/"+g+"."+f,caption=l)
        return "ok"
    except Exception as e:
        return e


@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/about')
def about():
    return 'About Page Route'


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
   
