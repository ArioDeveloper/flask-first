from flask import Flask , flash,request , jsonify , send_from_directory , url_for, render_template , redirect
import os
import sqlite3
import json
import re


app = Flask(__name__)

mainHale={"big":1,"bigLink":["c1","ng://negare.ng/d/1"], "smalls":[3,4 ],
                      "cs":[2,2,2,2,2]}

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = "files/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return '<h1><center>Home Page Route</h1></center>'

@app.route("/set",methods=["post"])
def set():
        if request.form["pas"] != "/)(+-&_$#@":
            return "by"
          
          
        big = request.form["b"]
        bl = json.loads(request.form["bl"])
        sm =json.loads(request.form["sm"])
        cs= json.loads(request.form["cs"])
       
        mainHale={"big":big,"bigLink":bl, "smalls":sm,
                      "cs":cs}
        

        
              
        return "ok: " + id
         


@app.route('/getPic')
def contact():
    picId = request.args.get('id')
    con= sqlite3.connect('profi.db')
    cur=con.cursor()
    cur.execute(f"SELECT *  FROM datas WHERE id= '{picId}'")
    d=cur.fetchall()[0]
    return  jsonify( d)


@app.route('/main' , methods=['GET'])
def api():
    con= sqlite3.connect('profi.db')
    cur=con.cursor()

    data={}
    data["big"]=[mainHale["big"],mainHale["bigLink"]]
    smals = []
    for i in mainHale["smalls"]:
        cur.execute(f"SELECT *  FROM datas WHERE id= '{i}'")
        d=cur.fetchall()
        
        smals.append(t2l(listMaker(d,8)))
        
    data["smals"] = smals
    
    cs = []
    cn =[]
    for i in mainHale["cs"]:
        cur.execute(f"SELECT * FROM datas WHERE c= '{i}'")
        d=cur.fetchall()
        
        cs.append(t2l(listMaker(d,8)))
        cur.execute(f"SELECT * FROM categorys WHERE id= '{i}'")
        d=cur.fetchall()
        
        cn.append(t2l(listMaker(d,8)))
        
        
    data["cs"]=cs
    
    data["cn"]=cn
    con.close()
    return  jsonify( data)
    pass
@app.route('/search' , methods=['GET'])
def searching():
    list=search(request.args.get('q'),num_results=30)
    return jsonify(list)
    
@app.route('/file/<path:path>',methods = ['GET','POST'])
def get_files(path):
    #con= sqlite3.connect('profi.db')
    #cur=con.cursor()
    #a=re.findall(r"(.*)\..*",path)[0]
    #cur.execute(f"SELECT dc FROM datas WHERE id= '{int(a)}'")
    #dc=cur.fetchall()[0]
    #dc =dc[0]+1
    #print(dc)
    #
    #cur.execute(f"UPDATE datas SET dc = '{dc}' WHERE id= '{int(a)}'")
    #con.commit()
    #con.close()

    """Download a file."""
    try:
        return send_from_directory("","files/" +path, as_attachment=True)
    except FileNotFoundError:
        abort(404)
        
        
@app.route('/image/<path:path>',methods = ['GET','POST'])
def get_images(path):

    """Download a file."""
    try:
        return send_from_directory("", "files/"+path, as_attachment=True)
    except FileNotFoundError:
        abort(404)
        
        
        
@app.route('/upload',methods=['POST'])
def upload_photo():
    if request.form["pas"] != "/)(+-&_$#@":
        return str(request.form["pas"])
    
    if not 'file' in request.files:
        flash('No File Part!')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image Successfully Uploaded and displayed below!')
        return "ok"
    else:
        flash('Allowed image types are : png, jpg, jpeg, gif')
        return redirect(request.url)
        
@app.route('/s' , methods=['GET'])
def search():
        con= sqlite3.connect('profi.db')
        cur=con.cursor()
        q= request.args.get('q')
        cur.execute(f"SELECT * FROM datas WHERE des LIKE '%{q}%'")
        d=cur.fetchall()
        con.close()
        d={"data":d}
        return jsonify(d)
        
        
def listMaker(lis, count):
    if len(lis) >= count:
        return lis[0:count]
        
    else:
        return lis[0:len(lis)]
        
def t2l(t):
        l=[]
        for i in t:
            
            l.append(list(i))
            
        return t
        
@app.route('/d' , methods=['GET'])
def d():
        con= sqlite3.connect('profi.db')
        cur=con.cursor()
        q= request.args.get('q')
        cur.execute(f"SELECT * FROM categorys")
        d=cur.fetchall()
        con.close()
        d={"data":d}
        return jsonify(d)
        
@app.route('/q' , methods=['GET'])
def q():
        con= sqlite3.connect('profi.db')
        cur=con.cursor()
        q= request.args.get('q')
        cur.execute(f"SELECT * FROM datas WHERE c LIKE '%{q}%'")
        d=cur.fetchall()
        con.close()
        d={"data":d}
        return jsonify(d)
        
@app.route("/ad",methods=["post"])
def add():
        if request.form["pas"] != "/)(+-&_$#@":
            return "by"
            
        con= sqlite3.connect('profi.db')
        cur=con.cursor()
        cur.execute("SELECT * FROM datas")
        lent = len(cur.fetchall())
        id = lent+1
        
        name = request.form["n"]
        c = request.form["c"]
        type = request.form["t"]
        iss= request.form["is"]
        iv = request.form["iv"]
        des = request.form["d"]
        cur.execute(f"INSERT INTO datas VALUES({id},'{name}','0',0,0,0,{type},'0','0',0,{iss},{c},{iv},'{des}','0') ")
        con.commit()
        #INSERT INTO projects(name,begin_date,end_date)
              #VALUES(?,?,?) 
              
        return f"ok: {id}"
         
         
@app.route("/ads",methods=["post"])
def adds():
        if request.form["pas"] != "/)(+-&_$#@":
            return "by"
            
        con= sqlite3.connect('profi.db')
        cur=con.cursor()
        cur.execute("SELECT * FROM categorys")
        lent = len(cur.fetchall())
        id = lent+1
        
        name = request.form["n"]
      
        cur.execute(f"INSERT INTO categorys VALUES({id},'{name}',0,'0') ")
        con.commit()
        #INSERT INTO projects(name,begin_date,end_date)
              #VALUES(?,?,?) 
              
        return f"ok: {id}"
         
        

    
if (__name__ =="__main__"):
    app.run(debug=False )
