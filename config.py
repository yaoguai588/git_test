# 数据库的配置
HOSTNAME = '192.168.0.172'
PORT = '3307'
DATABASE = 'forum'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "SDFASDFASDFASDFASDFASDF"

# 邮箱配置
# 本项目中用的是QQ邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "2584686736@qq.com"
MAIL_PASSWORD = "piwvoiukijwpebfb"
MAIL_DEFAULT_SENDER = "2584686736@qq.com"
