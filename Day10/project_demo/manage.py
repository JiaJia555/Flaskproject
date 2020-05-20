# 通过这个文件 去映射数据库
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from flask_app import app


# 映射那个模型 就把那个模型导入进来
from models import User


manage = Manager(app)

Migrate(app, db)

manage.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manage.run()

