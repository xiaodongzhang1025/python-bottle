#-*- coding: UTF-8 -*-
from bottle import Bottle, route, run, request, template, static_file
from time import localtime,strftime
app = Bottle()

@app.route('/')
@app.route('/hello/<name>')
def hello(name='dong'):
    print (request.method)  #POST
    #print (request.forms)  #post请求信息
    #print (request.query)  #get 请求数据
    #print (request.body)  #POST 请求数据
    #print (request.files)  #上传的文件信息
    #print (request.cookies)  #cookie信息
    #print (request.environ)  #环境信息
    #print (request.json)  #
    #print (request.params)  #
    print strftime("%Y-%m-%d %A %I:%M:%S",localtime())
    if request.method == "GET":
        #return 'hello, bottle-Get, %s'%strftime("%Y年%m月%d日 %A %I:%M:%S",localtime())
        #return template("<h1> Hello {{ name }}</h1>", name="Bottle")
        #return template('<b>Hello {{name}}</b>!', name=name)
        print "GET...name=%s"%name
        
    elif request.method == "POST":
        #return 'hello, bottle-Post, %s'%strftime(u"%Y年%m月%d日 %A %I:%M:%S",localtime())
        #return redirect("/index/")
        print "POST...name=%s"%name
    return static_file("index.html", root='./html/')
    
##########################################################
@app.route('/login', method='POST')
def login():
    print (request.method)  #POST
    #print (request.forms)  #post请求信息
    #print (request.query)  #get 请求数据
    #print (request.body)  #POST 请求数据
    #print (request.files)  #上传的文件信息
    #print (request.cookies)  #cookie信息
    #print (request.environ)  #环境信息
    #print (request.json)  #
    #print (request.params)  #
    print strftime("%Y-%m-%d %A %I:%M:%S",localtime())
    if request.method == "GET":
        print "GET..."
    elif request.method == "POST":
        print "POST..."
    username=request.forms.get('username')
    password=request.forms.get('password')
    print "username", username
    print "password", password
    return "username=%s, password = %s"%(username, password)
    
if __name__ == '__main__':
    run(app, host = 'localhost', port = 8899)