from flask import Blueprint, render_template

# 在当前目录建立模板目录lgcoder
# 如果默认目录templates有news文件就会优先调用templates里的文件，没有会调用设置的目录下的文件，都没有就会报错
news_bp = Blueprint('news', __name__, url_prefix="/news", template_folder="lgcoder", static_folder='static')


# /news url_prefix / ==>/news/
@news_bp.route("/")
def news():
    # return "新闻首页"
    return render_template("news.html")