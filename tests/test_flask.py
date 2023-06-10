import unittest
from flask import Flask, url_for, session
from flask_testing import TestCase
import src.flask_app


class FlaskAppTests(TestCase):
    def create_app(self):
        return src.flask_app.app

    def test_index(self):
        with self.client:
            response = self.client.get('/', follow_redirects=False)
            self.assertIn(response.status_code, [301, 302, 303, 305, 307])
            self.assertEqual(response.location, '/login')

    # def test_login(self):
    #     with self.client:
    #         response = self.client.get('/login')
    #         self.assertEqual(response.status_code, 200)
    #         self.assert_template_used('login.html')
    #         self.assertIn('auth_url', session)

    # def test_authorized(self):
    #     with self.client:
    #         response = self.client.get('/authorized')
    #         self.assertRedirects(response, url_for('index'))

    # def test_logout(self):
    #     with self.client:
    #         response = self.client.get('/logout')
    #         self.assertRedirects(response, 'https://login.microsoftonline.com/oauth2/v2.0/logout')

    # def test_dashboard(self):
    #     with self.client:
    #         response = self.client.get('/dashboard')
    #         self.assertEqual(response.status_code, 200)
    #         self.assert_template_used('dashboard.html')
    #         self.assertIn('chart_base64', response.get_data(as_text=True))
    #         self.assertIn('user', response.get_data(as_text=True))

    # def test_update_piechart(self):
    #     with self.client:
    #         response = self.client.post('/update_piechart', data={
    #             'user': 'test_user',
    #             'category': 'test_category',
    #             'value': '50'
    #         })
    #         self.assertRedirects(response, '/plotly')

    # def test_plotly(self):
    #     with self.client:
    #         response = self.client.get('/plotly')
    #         self.assertEqual(response.status_code, 200)
    #         self.assert_template_used('plotly.html')
    #         self.assertIn('chart_html', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()