from flask_script import Manager

from flask_script_demo import app, AdminUser, db


manage = Manager(app)

@manage.option('-u', '--name', dest='name')
@manage.option('-e', '--email', dest='email')
def add_user(name, email):
    user = AdminUser(name=name, email=email)
    db.session.add(user)
    db.session.commit()

if __name__ =='__main__':
    manage.run()


# cd flask_add_admin
# python manage.py add_user -u fu -e 123@qq.com