from flask import Blueprint
# 1.定义蓝图对象
home = Blueprint("home", __name__)

# 4.关联视图函数,放在创建之后########
import app.home.views
# 另一种导入方式
# from .views import *