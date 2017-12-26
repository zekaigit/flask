#coding=utf-8
from app import app
from flask import render_template

#两个 route 装饰器创建了从网址 / 以及 /index 到这个函数的映射
@app.route('/')
@app.route('/index')
#def index():
#	return "Hello,World!"

#def index():
#   user = { 'nickname': 'Miguel' } # fake user
#   return '''
#<html>
#  <head>
#    <title>Home Page</title>
#  </head>
#  <body>
#    <h1>Hello, ''' + user['nickname'] + '''</h1>
#  </body>
#</html>
#'''

def index():
	user={'nickname':'Miguel'}
	posts = [
		{
			'author':{'nickname':'john'},
			'body':'Beautiful day in Portland!'
		},
		{
			'author':{'nickname':'Susan'},
			'body':'The Avenger movies was so cool!'
		}
	]
	return render_template("index.html",
		title = 'Home',
		user=user,
		posts=posts)