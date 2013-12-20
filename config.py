import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_SECRET_KEY = 'ansible key'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://db_user:password@192.168.113.132/ansible_flask'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')