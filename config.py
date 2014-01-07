import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_SECRET_KEY = 'ansible key'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://db_user:some_pass@192.168.180.131/ansible_flask'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')