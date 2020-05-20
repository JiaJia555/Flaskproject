from flask_script import Manager

from flask_sqlalchemy_demo import app



manage = Manager(app)

@manage.command
def index():
    print('hello')


# -n 是 --name 的简称
@manage.option('-n', '--name', dest='name')
@manage.option('-u', '--url', dest='url')
def hello(name, url):
    print("hello", name, url)

# 创建超级管理员 如何创建

if __name__ == '__main__':
    manage.run()

# 运行
# cd E:\PythonProjects\Flask框架\Day10
# ls
# python manage.py index
# python manage.py hello -n fu -u www.baidu.com

