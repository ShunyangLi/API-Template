from app import mail
from threading import Thread
from flask import render_template
from flask_mail import Message


# 异步发送
def async_start(app, msg):
    with app.app_context():
        mail.send(msg)

# **kwargs 指传进来的参数, 可以传多个参数进来。eg: username = 'xxx', link = 'xxx.com'
def send(to, subject, template, **args):
    msg = Message(subject, sender = '123456@qq.com', recipients=[to])
    msg.html = render_template(template, **args)
    thread = Thread(target=async_start, args=[app, msg])
    thread.start()
    return thread


"""
一个简单的例子：
send('123456@qq.com', 'Hello world', 'hello.html', username='xxx')
简单解释一下：
    hello.html是需要在templates里面定义好的，其格式是我们jinja2的模板样式。参数形式也一样
    在hello.html之后可以添加多个参数，比如username='xx', email='xx'.
    我已经在templates里面写好了一个html
"""

