# import unittest
# import src.flask_app
# from flask import Flask, url_for
# from tests.test_flask import FlaskAppTests


# class TestFlaskSSO(FlaskAppTests):
#     def test_dashboard_redirect_to_login(self):
#         # Simulate the case when token is not available
#         with self.app.test_request_context():
#             with self.app.test_client() as client:
#                 response = client.get('/dashboard')
#                 self.assertRedirects(response, url_for('login'))

#     def test_dashboard_template_rendered(self):
#         # Simulate the case when token is available
#         with self.app.test_request_context():
#             with self.app.test_client() as client:
#                 # Mock the _get_token_from_cache() function to return a token
#                 src.flask_app._get_token_from_cache = lambda scope: ('mock_token', [])
#                 response = client.get('/dashboard')
#                 self.assertEqual(response.status_code, 200)
#                 self.assertIn(b'dashboard.html', response.data)


# if __name__ == "__main__":
#     unittest.main()
