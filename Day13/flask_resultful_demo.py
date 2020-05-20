from flask import Flask, render_template, url_for
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
import config
from exts import db
from models import Article

app = Flask(__name__)
# 加载配置文件
app.config.from_object(config)

db.init_app(app)

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
        # 'title': fields.String,
        # 重命名
        'article_title': fields.String(attribute='title'),
        'content': fields.String,
        # 'author': fields.String,
        'author': fields.Nested({
            "username": fields.String,
            'email': fields.String
        }),
        # 'tags': fields.String
        'tags': fields.List(fields.Nested({
            "id": fields.Integer,
            'name': fields.String,
        })),
        # 默认值 模型中已经有值得变量默认值不会显示
        'read_count': fields.Integer(default=0)
    }

    # 即使content没有设置值，也会返回 none
    @marshal_with(resource_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        # return {"title": "juran"}
        return article

api.add_resource(IndexView, '/', endpoint='index')
api.add_resource(ArticleView, '/article/<article_id>', endpoint='article')


if __name__ == '__main__':
    app.run(debug=True)