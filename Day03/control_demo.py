from flask import Flask, render_template

app = Flask(__name__)
# 模板文件自动更新
app.config["TEMPLATES_AUTO_RELOAD"] = True

# 1. if_for语句
@app.route("/")
def index():
    context = {
        "username":"jiajia",
        "books":["Python","Java","PHP"],
        "users":{
            "name": "jiajia",
            "age": 18,
            "address": "csc"
    }
    }
    return render_template("if_for.html", **context)


# 2.for循环

# 3.宏
@app.route("/macro/")
def macro():
    return render_template("macro.html")
# with context导入username值=jiajia

# 4.include 只能相对于templates这个目录来写绝对路径
# 模板中set定义全局变量优先，这里不会显示lgcoder,with定义局部,和全局是独立的，互不影响
# set 只能定义一个变量
@app.route("/detail/")
def detail():
    return render_template("detail.html", name="lgcoder")

if __name__== '__main__':
    app.run(debug=True)