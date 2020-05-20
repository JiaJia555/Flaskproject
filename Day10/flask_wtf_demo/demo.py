from flask import Flask, request, render_template
from forms import RegistForm, LoginForm
app = Flask(__name__)

@app.route("/")
def index():
    return "首页"


# 接收GET请求
@app.route("/regist/", methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return "success"
        else:
            # 打印验证的错误信息
            print(form.errors)
            return "fail"
        # 只需要一个验证的结果
        # username = request.form.get('username')
        # password = request.form.get('password')
        # password_confirm = request.form.get('password_confirm')
        #
        # if len(username) < 3 or len(username) > 10:
        #     return "用户名不正确"
        # if password != password_confirm:
        #     return "两次密码不一致"
        # if len(password) < 3 or len(password) > 10:
        #     return "密码长度不正确"

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return 'fail'

if __name__ == '__main__':
    app.run(debug=True)