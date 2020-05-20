from wtforms import Form, StringField, IntegerField, validators
from flask import request
from wtforms.validators import length, Regexp, EqualTo, Email, NumberRange, InputRequired, URL, ValidationError

# 表单验证
class RegistForm(Form):
    username = StringField(validators=[length(min=3, max=10, message="用户名长度不正确")])
    password = StringField(validators=[length(min=3, max=10, message="密码长度不正确")])
    password_confirm = StringField(validators=[length(min=3, max=10, message="密码长度不对"), EqualTo('password', message="两次密码不一致")])


class LoginForm(Form):
    # email = StringField(validators=[Email()])
    # age = IntegerField(validators=[NumberRange(1, 120, message="年龄范围错误")])
    # username = StringField(validators=[InputRequired(message='用户名不能为空')])
    # phone = StringField(validators=[Regexp(r'1[38]\d{9}')])
    # info = StringField(validators=[URL()])
    # 验证码
    captcha = StringField(validators=[length(min=4,max=4)])
    # print(type(captcha))            # <class 'wtforms.fields.core.UnboundField'>
    # 内容    4587  不能直接这样验证
    # if captcha =='4587':
    #     print("验证码正确")
    # else:
    #     print("验证码错误")
    def validate_captcha(self, field):      # 方法名不是随便定义的，validate_+ 验证字段
        print(type(field))      # <class 'wtforms.fields.core.StringField'>
        if field.data != '4587':
            raise ValidationError("验证码错误")
        else:
            print("验证成功")


