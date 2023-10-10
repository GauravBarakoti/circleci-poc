import unittest
from Flask_application import app

class TestMyFlaskApplication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Application Up and Running with no downtime, ============= smmooothhh  Yay!!')

if __name__ == '__main__':
    unittest.main()
