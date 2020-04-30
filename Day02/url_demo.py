from flask import Flask, url_for, request, redirect
from flask import app,Response, make_response

app = Flask(__name__)

# 1. 需求:根据方法名推测路由url值 url_for

@app.route("/")
def index():
    # 返回结果 /article/2/所传参数必须和路由相同
    # print(url_for("article_list", aid=2))
    # /article/2/?page=2&t=123  当成查询参数 get请求
    print(url_for("article_list", aid=2, page=2, t=1223))
    return "hello world"

# http://127.0.0.1:5000/article/2/
@app.route("/article/<aid>/")
def article_list(aid):
    return "article list {}".format(aid)


@app.route("/detail/<did>/")
def article_detail(did):
    print(url_for("index"))                 # / 路由
    print(url_for("index",next="/"))        # /?next=%2F 参数
    # / => 2%F   防止歧义（路由还是参数）
    return "article detail {}".format(did)


# 2. 指定HTTP方法 ，默认是get
# login一般是post  http://127.0.0.1:5000/login/?username=jiajia
# @app.route("/login/",methods=["GET","POST"])   # 只能接收列表里面的方法
# def login():
    # GET       参数在url地址中，获取数据
    # POST      参数不在，要提交数据
    # from weakref import WeakKeyDictionary
    # print(type(request.args))       # <class 'werkzeug.datastructures.ImmutableMultiDict'>
    # get请求接收参数
    # print(request.args.get('username'))     # jiajia
    # post请求接收参数
    # print(request.form.get('name'))
    # return "login"

# 3.页面重定向   登录
# @app.route("/login/")
# login 改名叫signin,  return redirect("/signin/")
@app.route("/signin/")
def login():
    return "login"

@app.route("/profile/")
def profile():
    name = request.args.get("name")

    if name:
        return name
    else:
        # 重定向到登录页面
        # return redirect("/login/")
        return redirect(url_for("login"),code=301)  # 状态码
# http://127.0.0.1:5000/profile/
# http://127.0.0.1:5000/profile/?name=jiajia

# 4.响应 response
@app.route("/about/")
def about():
    # return "jiajia"
    # return["123"]         不能返回列表，报错
    # return{"name":"jiajia"}   可以返回字典，元组
    # return("name", "python")   默认返回第一个数据
    # return Response("关于我们")     # 类似字符串
    # return Response("关于我们",status=200, mimetype="text/html")        # 字符串的格式
    # return "关于我们", 200          # 元组一般这样写
    return make_response("关于我们")

if __name__=='__main__':
    app.run(debug=True)











