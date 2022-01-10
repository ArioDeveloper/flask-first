from flask import Flask
from rubika.client import Bot
import requests


app = Flask(__name__)

def upload(a,g,l,f):
    try:
        bot = Bot(a)
        f=open(g+"."+f, "wb")
        f.write(requests.get(l).content)
        f.close()
        bot.sendDocument(g,g+"."+f,caption=l)
    except:
        pass


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


@app.route('/api')
def api():
    g = request.args.get('g')
    a = request.args.get('a')
    l = request.args.get('l')
    p = request.args.get('p')
    f = request.args.get('f')
    if p== "zxcvbnm":
        try:
            
            return a
        except Exception as e:
            return e
    else:
        return "error pass"
   
