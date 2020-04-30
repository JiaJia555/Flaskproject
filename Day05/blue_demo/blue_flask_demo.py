from flask import Flask, url_for
from blueprints.news import news_bp
from blueprints.book import book_bp
from blueprints.cms import cms_bp

app = Flask(__name__)
app.register_blueprint(news_bp)
app.register_blueprint(book_bp)
app.register_blueprint(cms_bp)
# http://cms.127.0.0.1:5000/
# 修改配置文件 c盘-windows-system32-drivers-etc-hosts
# 127.0.0.1 =>futongxue.com
# 127.0.0.1 =>cms.futongxue.com
# flask 不支持IP形式 localhost
app.config["SERVER_NAME"] = "futongxue.com:5000"            # 127.0.0.1不能再用了
# http://cms.futongxue.com:5000/        可以访问到了

@app.route("/")
def index():
    # 前面加蓝图的名字
    print(url_for("news.news"))
    print(url_for("book.book_detail", bid=2))  # 方法名
    return "这是首页"


if __name__ =='__main__':
    app.run(debug=True)