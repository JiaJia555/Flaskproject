from flask import Flask, render_template
# 1. templates目录名是固定的
app = Flask(__name__)
# 默认文件夹可以修改写绝对路径/相对路径,一般不改
# app = Flask(__name__, template_folder="C:\Users\shelleyfu\Downloadbyjia\Flask框架\Day02\templates\profile")
# app = Flask(__name__, template_folder=r"./demo")
@app.route("/")
def index():
    # return '<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">'
    # 默认存在templates目录找模板文件
    # return render_template("index.html"
    # return render_template("index.html", username="逻辑教育", age = "18")#传参
    # 这样写太复杂，可以全部写在context
    context = {
        "username":"逻辑教育",
        "age": 18,
        "books": {
            "Python":23,
            "Java": 24,
            "PHP": 25
        },
        "book":["Python", "Java", "PHP"]
    }
    # return render_template("index.html", context=context)
    # **会自动将字典变成username:"逻辑教育"这样的格式
    return render_template("index.html", **context)
@app.route("/profile/")
def profile():
    return render_template("profile/user.html")     # 需要传路径

# 2.模板传参
# 2.1参数是字典
# 2.2 字典嵌套字典取值
# 2.3 列表取值
if __name__=="__main__":
    app.run(debug=True, port=8000)