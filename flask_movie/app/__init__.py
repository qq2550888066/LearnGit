from flask import Flask, render_template

app = Flask(__name__)

# 导包: 优先从home 或 admin 的init.py文件中找home或admin
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 3. 注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


@app.errorhandler(404)
def get_error(error):
    return render_template("home/404.html"), 404
