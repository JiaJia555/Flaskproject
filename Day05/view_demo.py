from flask import Flask, url_for,views,jsonify
from flask import render_template, request
# from flask.views import MethodView
# from functools import wraps

app = Flask(__name__)


@app.route("/")
def index():
    # print(url_for("profile"))
    # 如果add_url_rule给了endpoint,相当于给url起了一个名字
    # print(url_for("geren"))
    # print(url_for("list1"))
    # print(url_for("list2"))
    return "首页"


# 4.登陆之后才能访问的装饰器(函数）
def login_required(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get("username")
        if username:
            return func(*args, **kwargs)
        else:
            return "请先登录"
    return wrapper

@app.route("/settings/")
@login_required
def setting():
    return "个人中心设置"



# def profile():
#     return "个人中心"


class ListView(views.View):
    def dispatch_request(self):
        # return self.demo()   返回测试
        return "类视图"

    def demo(self):
        return "测试"

# 1. 类视图返回Jason数据
class JsonView(views.View):

    def get_response(self):
        raise NotImplementedError()

    def dispatch_request(self):
        response = self.get_response()
        return jsonify(response)


class ListJsonView(JsonView):
    def get_response(self):
        return {"username":"jiajia"}

# 2. 返回公共变量
class BaseView(views.View):
    def __init__(self):
        # python2
        # super(BaseView, self).__init__()
        super().__init__()
        self.context = {
            "name": "jiajia"
        }

# class LoginView(BaseView):
#     def dispatch_request(self):
#         return render_template("login.html", **self.context)


class RegistView(BaseView):
    def dispatch_request(self):
        return render_template("regist.html", **self.context)

# 3. 基于调度方法的视图
class LoginView(views.MethodView):
    # def rend_temp(self, *args, **kwargs):
    #     return render_template("login.html")

    def get(self, error=None):
        return render_template("login.html", error = error)

    def post(self):
        name = request.form.get("name")
        password = request.form.get("password")
        # 查询数据库，验证输入是否正确
        if name == "jiajia" and password == "123":
            return "登录成功"
        else:
            # return "账号或密码错误"
            # return render_template("login.html",error="账号或密码错误")
            return self.get("账户莫玛错误")

class ProfileView(views.View):
    # 在类中用装饰器
    decorators = [login_required]

    def dispatch_request(self):
        return "个人页面"




# 添加URL规则
# app.add_url_rule("/profile/", endpoint="geren", view_func=profile)
# url_for方法名优先用endpoint给定的值，没有再用view_func给的值
# app.add_url_rule("/list/",view_func=ListView.as_view('list2'))
app.add_url_rule("/list/",endpoint="list1", view_func=ListView.as_view('list2'))
# 类视图返回Jason数据
app.add_url_rule("/listjson/", view_func=ListJsonView.as_view('listjson'))
# 返回公共变量
# app.add_url_rule("/login/", view_func=LoginView.as_view(('login')))
app.add_url_rule("/regist/", view_func=RegistView.as_view(('regist')))

app.add_url_rule("/login/", view_func=LoginView.as_view(('login')))

app.add_url_rule("/profile/", view_func=ProfileView.as_view('profile'))

if __name__=='__main__':
    app.run(debug=True)

