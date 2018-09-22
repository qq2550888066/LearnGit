from flask import Blueprint

# 1.定义蓝图对象
admin = Blueprint("admin", __name__)

# 4.关联视图函数
import app.admin.views
