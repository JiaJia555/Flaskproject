from flask import Flask, render_template, url_for
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with

app = Flask(__name__)
# 用Api来绑定app
api = Api(app)

class IndexView(Resource):
    def get(self):
        return {"username":"futongxue"}

    def post(self):
        parse = reqparse.RequestParserequest()
        # type 类型
        # help 错误信息
        parse.add_argument('username', type=str, help='用户名验证错误', required=True)
        parse.add_argument('password', type=str, help='密码错误')
        parse.add_argument('age', type=int, help='年龄错误', default=18)
        parse.add_argument('gender', type=str, help='性别有误', choice=['male', 'female', 'secret'])
        # email url regex
        parse.add_argument('homepage', type=inputs.url, help='url有误')
        parse.add_argument('phone', type=inputs.regex(r'1[3]\d{9}'), help='手机号码有误')
        args = parse.parse_args()
        print(args)
        return {"info": "登录成功"}


class ArticleView(Resource):
    resource_fields = {
        'title': fields.String,
        'content': fields.String
    }

    # 即使content没有设置值，也会返回 none
    @marshal_with(resource_fields)
    def get(self):
        return {"title": "juran"}


api.add_resource(IndexView, '/', endpoint='index')
api.add_resource(ArticleView, '/article/', endpoint='article')


if __name__ == '__main__':
    app.run(debug=True)