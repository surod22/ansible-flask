import unittest
from app import app


class AnsibleTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_see_data_from_table(self):

        table_dictionary = {'ipaddress':'127.0.0.1','hostname':'localhost','proxypath':'localhost.thoughtworks.com'}
        response = self.client.get('/')
        #self.assertEqual(self.get_context_variable('ipaddress'), '127.0.0.1')
        for name in table_dictionary:
            assert name in response.data
            assert table_dictionary[name] in response.data

if __name__ == '__main__':
    unittest.main()



