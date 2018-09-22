# 导包,优先从app包的init.py文件中导入app,
from app import app

# 启动程序
if __name__ == '__main__':
    app.run(debug=True)
