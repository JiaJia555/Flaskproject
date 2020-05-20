# MYSQL的配置项
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0058'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# engine = create_engine(DB_URL)
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False