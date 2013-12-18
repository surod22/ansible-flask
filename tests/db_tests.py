import unittest
from app import app, db
from app.models import Server, Value


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSR_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db_user:password@192.168.113.131/ansible_test'
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_should_see_data_when_inserted(self):
        expected_result = {u'ipaddress':u'127.0.0.1',u'hostname':u'localhost',u'proxypath':u'localhost.thoughtworks.com'}

        test_server = Server('confTest')
        test_server.ipaddress = '127.0.0.1'
        test_server.hostname = 'localhost'
        test_server.variables['proxypath'] = Value('localhost.thoughtworks.com')
        db.session.add(test_server)
        db.session.commit()

        self.assertEqual(test_server.variables, expected_result)

if __name__ == '__main__':
    unittest.main()
