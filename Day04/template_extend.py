
from flask import Flask, render_template
# static_folder="" 修改static目录位置
app = Flask(__name__)

app.config["TEMPALTES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list/")
def list_article():
    return render_template("list.html")


if __name__=='__main__':
    app.run(debug=True)

# 1.模板继承
#     子模版不能直接修改父模板的内容
#     子模版通过block修改里面的内容，可以全部修改
#     可以嵌套但是不能重名
#     子模板不可以自己定义block和标签，不会显示
#     子模版不可以继承多个父模板
#     {{ super() }}调用父模板的block
#     模板继承放到Block代码块的上面
# 参考链接
# https://blog.csdn.net/weixin_43883022/article/details/89703725






















