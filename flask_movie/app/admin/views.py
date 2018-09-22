# 定义视图
#  . 表示从当前文件所在包的init.py中导入
from . import admin
from flask import Flask, render_template, url_for, redirect


# 2.使用蓝图对象来装饰路由
# 注册路由,指定静态文件夹,注册模板过滤器
@admin.route("/")
def index():
    return "<h1 style:color='red'>this is admin</h1>"


# 登录界面
@admin.route("/login")
def login():
    return render_template("admin/login.html")


# 登出界面
@admin.route("/logout")
def logout():
    return redirect(url_for("admin.login"))
