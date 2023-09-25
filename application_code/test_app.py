import unittest
from app import application
from app.forms import SignUpForm
from flask_testing import TestCase

class TestApp(TestCase):

    def create_app(self):
        application.config['TESTING'] = True
        application.config['WTF_CSRF_ENABLED'] = False
        return application

    def test_home_page(self):
        response = self.client.get('/home')
        self.assert200(response)
        self.assert_template_used('home.html')

    def test_sign_up_page(self):
        response = self.client.get('/signup')
        self.assert200(response)
        self.assert_template_used('signup.html')

    def test_sign_up_submission(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'country': 'United States',
            'newsletter': True
        }
        response = self.client.post('/signup', data=form_data, follow_redirects=True)
        self.assert200(response)
        self.assert_template_used('home.html')

if __name__ == '__main__':
    unittest.main()
