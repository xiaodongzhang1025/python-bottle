#-*- coding: UTF-8 -*-
from bottle import Bottle, route, run, request, template, static_file
from time import localtime,strftime
import os
app = Bottle()

@app.route('/')
@app.route('/<path>', method='POST')
def index(path='index'):
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
        print "GET...path=%s"%path
    elif request.method == "POST":
        print "POST...path=%s"%path
    
    #return static_file("%s.html"%path, root='./html/')
    current_folder = os.path.dirname(os.path.abspath(__file__))   
    static_file = os.path.join(current_folder, './html/%s.html'%path)
    print static_file
    with open (static_file) as f:
        content = f.read()
    return content
    
##########################################################

@app.route('/login', method='POST')
def login():
    print (request.method)  
    print strftime("%Y-%m-%d %A %I:%M:%S",localtime())
    if request.method == "GET":
        print "GET..."
    elif request.method == "POST":
        print "POST..."
    username=request.forms.get('username')
    password=request.forms.get('password')
    shellcmd=request.forms.get('shellcmd')
    shellret=''
    
    f = os.popen(shellcmd, 'r')
    shellret = f.read().decode('gbk')
    f.close()
    print "username", username
    print "password", password
    print "shellcmd", shellcmd
    print "shellret", shellret
    #return "username=%s, password = %s"%(username, password)
    content = """
<p>username is :{{username}}</p>
<p>password is :{{password}}</p>
<p>shellcmd is :{{shellcmd}}</p>
<p>shellret is :{{shellret}}</p>
"""
    return template(content, username = username, password = password, shellcmd=shellcmd, shellret=shellret)


if __name__ == '__main__':
    run(app, host = 'localhost', port = 8899)