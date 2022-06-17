from unittest import TestCase

from app import app

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class CoverterTestCase(TestCase):
    """Test flask app of currency converter"""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure home page with conversion form is displayed correctly"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('currency converter homepage', html)
            self.assertIn('<form', html)

    def test_correct_results(self):
        """Check if results page correctly returned,
             assuming form filled out correctly"""

        with app.test_client() as client:

            conv_response = client.post(
                '/results',
                data={
                    "conv-from": "USD",
                    "conv-to": "EUR",
                    "amount": "100"
                })
            html = conv_response.get_data(as_text=True)
            self.assertEqual(conv_response.status_code, 200)
            self.assertIn('results page', html)

    def test_incorrect_results_redirect(self):
        """Check if successfully redirected to homepage with flashed
            message if form values incorrect"""

        with app.test_client() as client:

            # Checks conv-from input
            conv_response = client.post(
                '/results',
                data={
                    "conv-from": "DOG",
                    "conv-to": "USD",
                    "amount": "100"
                },
                follow_redirects=True
            )
            html = conv_response.get_data(as_text=True)

            self.assertEqual(conv_response.status_code, 200)
            self.assertIn('Starting currency not valid', html)
            self.assertIn('currency converter homepage', html)

            # Checks conv-to input
            conv_response = client.post(
                '/results',
                data={
                    "conv-from": "USD",
                    "conv-to": "DOG",
                    "amount": "100"
                },
                follow_redirects=True
            )
            html = conv_response.get_data(as_text=True)

            self.assertEqual(conv_response.status_code, 200)
            self.assertIn('Target currency not valid', html)
            self.assertIn('currency converter homepage', html)

            # Checks amount input
            conv_response = client.post(
                '/results',
                data={
                    "conv-from": "USD",
                    "conv-to": "EUR",
                    "amount": "dog"
                },
                follow_redirects=True
            )
            html = conv_response.get_data(as_text=True)

            self.assertEqual(conv_response.status_code, 200)
            self.assertIn('Not a valid amount', html)
            self.assertIn('currency converter homepage', html)
