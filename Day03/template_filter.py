from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
# 配置文件 模板文件自动更新
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    context = {
        "username":"hello jiajia",
        "age": -18,
        # "name": "lgcoder"
        # "name": ""      # 什么都不显示
        "name":None,         # 显示None，
        "es": "<script>alert('hello')</script>",
        "h1":"<h1>hello</h1>",
        "books":["Python","Java","PHP"],
        "address": "长沙市岳麓区",
        "now_time": datetime(2020, 4, 18, 22, 10)
    }
    return render_template("index.html", **context)

# 自己定义模板过滤器
@app.template_filter("my_cut")
def cut(value):
    return value.replace("hello", "")


@app.template_filter("handle_time")
def handle_time(time):
    """
    小于1分钟--刚刚
    大于1分钟小于1小时--xx分钟之前
    大于1小时小于24小时--xx小时之前
    :param time:
    :return:
    """
    if isinstance(time, datetime):
        now =datetime.now()
        # 得到总秒数
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif timestamp >=60 and timestamp <= 60*60:
            return "%s分钟之前" % int(timestamp/60)
        elif timestamp >= 60*60 and timestamp <=60*60*24:
            return "%s小时之前" % int(timestamp/(60*60))
    else:
        return time

if __name__== '__main__':
    app.run(debug=True)





