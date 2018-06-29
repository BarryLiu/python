from flask import Flask
from flask import render_template
from flask import request


from flask import abort, redirect, url_for

"""
http://www.pythondoc.com/flask/index.html
简单使用, 请求,响应,请求传参,重定向,404页面
"""

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

# 正常返回数据
@app.route("/")
def index():
    return render_template('01hello.html',name="tom")
@app.route("/index")
def index2():
    return render_template('01hello.html',name="tom2")

# 获取数据返回
@app.route("/hello1/<name>")
def hello1(name=None):
    print("print name : ",name)
    return render_template('01hello.html',name=name)

# 获取表单数据返回
@app.route("/hello2",methods=['POST', 'GET'])
def hello2():
    name = request.form['name']
    print("print name : ",name)
    return render_template('01hello.html',name=name)

# 重定向
@app.route("/hello3")
def hello3():
    return redirect(url_for('index'))

#404 页面找不到
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

#
@app.route("/hello4")
def hello4():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug=True
    app.run()