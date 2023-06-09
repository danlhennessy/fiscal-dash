import unittest
from flask import Flask, url_for
import src.flask_app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_dashboard_route(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_redirect_to_login(self):
        # Simulate the case when token is not available
        with self.app.test_request_context():
            with self.app.test_client() as client:
                response = client.get('/dashboard')
                self.assertRedirects(response, url_for('login'))

    def test_dashboard_template_rendered(self):
        # Simulate the case when token is available
        with self.app.test_request_context():
            with self.app.test_client() as client:
                # Mock the _get_token_from_cache() function to return a token
                src.flask_app._get_token_from_cache = lambda scope: ('mock_token', [])
                response = client.get('/dashboard')
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'dashboard.html', response.data)

    def test_dashboard_chart_data(self):
        # Simulate the case when token is available
        with self.app.test_request_context():
            with self.app.test_client() as client:
                # Mock the _get_token_from_cache() function to return a token
                src.flask_app._get_token_from_cache = lambda scope: ('mock_token', [])
                response = client.get('/dashboard')
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'chart_base64', response.data)
                self.assertIn(b'user', response.data)
                
