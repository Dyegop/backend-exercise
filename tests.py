import unittest
from app import app


class BasicTests(unittest.TestCase):
    def setUp(self):
        """ Set up configurations before running tests"""
        app.config.update(TESTING=True, DEBUG=False)
        self.app = app.test_client()

    def tearDown(self):
        """ Execute code something after each test"""
        pass

    def test_root(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)




if __name__ == "__main__":
    unittest.main()
