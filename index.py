from pytube import YouTube  
from flask import Flask , json , request
import re
app = Flask(__name__)


@app.route('/api')
def home():
    url = request.args.get("url")
    youtube_obj = YouTube(video_url)
    links={}
    for stream in youtube_obj.streams:
    
        mime =re.findall('mime_type="(.*?)?"',str(stream))[0]
        try:
            res=re.findall('res="(.*?)?"',str(stream))[0]
        except:
            res=""
        url = stream.url
        sub=mime+" : "+res
        links[sub]=url
    
    return str(links)

app.run()
