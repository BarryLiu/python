from flask import Flask

"""
session 文件上传 Cookies 消息闪烁 日志
"""
app =Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)


