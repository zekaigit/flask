#coding=utf-8
## 简单地创建应用对象，接着导入视图模块
from flask import Flask

app=Flask(__name__)
from app import views
