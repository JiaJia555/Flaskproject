from flask import g


# utils 工具文件 生成24位字符串 发送验证码
# def log_a(username):
#     print("log_a %s" % username)
#
# def log_b(username):
#     print("log_b %s" % username)

def log_a():
    print("log_a %s" % g.username)

def log_b():
    print("log_b %s" % g.username)