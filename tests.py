import unittest
import database as db
from app import app, es


class BasicTests(unittest.TestCase):
    def setUp(self):
        """ Set up configurations before running tests"""
        app.config.update(TESTING=True, DEBUG=False)
        self.app = app.test_client()

    def tearDown(self):
        """ Execute code something after each test"""
        pass

    def test_es_connection(self):
        """ Test connection to ElasticSearch"""
        self.assertTrue(es.ping())

    def test_es_response(self):
        """ Test elastic results - must be 20 """
        for j in range(0, 250):
            es_rawData = db.getData(j, es)
            es_results = [i['_source'] for i in es_rawData['hits']['hits']]
            self.assertEqual(len(es_results), 20)

    def test_flask_home(self):
        """ Test response for home url """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_flask_endpoint_html(self):
        """ Test response for API endpoint with 'HTTP_ACCEPT': 'text/html' """
        response = self.app.get('/data/0', environ_base={'HTTP_USER_AGENT': 'Chrome, etc',
                                                         'HTTP_ACCEPT': 'text/html'})
        self.assertEqual(response.status_code, 200)

    def test_flask_endpoint_json(self):
        """ Test response for API endpoint with 'HTTP_ACCEPT': 'text/html' """
        response = self.app.get('/data/0', environ_base={'HTTP_USER_AGENT': 'Chrome, etc',
                                                         'HTTP_ACCEPT': 'application/json'})
        self.assertEqual(response.status_code, 200)






if __name__ == "__main__":
    unittest.main()

