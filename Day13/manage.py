from flask_script import Manager
from flask_resultful_demo import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
# 导入模型
import models

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()