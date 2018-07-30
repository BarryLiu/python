# all the imports
# http://www.pythondoc.com/flask/tutorial/dbinit.html 两种方式创建数据库: 1.sqlite3 命令,2.用地址中contextlib 包
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'dream123'


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# -------请求之前连接数据库和请求之后关闭数据库--------
@app.before_request
def before_request():
    print("请求数据库连接...")
    g.db = connect_db()

# 请求出错就不会进
@app.after_request
def after_request():
    print("请求数据库连接...")
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    print("关闭数据库连接...")
    g.db.close()







if __name__ == '__main__':
    app.run()