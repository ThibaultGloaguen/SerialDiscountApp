from application import app
import os
import unittest


class TestRoute(unittest.TestCase):
    app.config['DATABASE_DISCOUNT'] = os.path.join(app.root_path, '../discount_codes_test.db')
    app.config['DATABASE_SERIAL'] = os.path.join(app.root_path, '../serial_discount_test.db')
    client = app.test_client()

    def test_no_serial_in_route(self):
        rv = self.client.get('/discount')
        self.assertEqual(rv.get_json(), {'error': 'Please enter a serial number'})
        self.assertEqual(rv.status_code, 400)

    def test_wrong_serial_in_route(self):
        rv = self.client.get('/discount?serial_number=wrong')
        self.assertEqual(rv.get_json(), {'error': 'The serial number wrong is unknown'})
        self.assertEqual(rv.status_code, 404)

    def test_good_serial(self):
        rv = self.client.get('/discount?serial_number=5ad/602d79c8-AX-b97c747299-d4250111d8f-CQ')
        self.assertEqual(rv.get_json(), {'discount': 'pwYT9-CvnSS4oHL'})
        self.assertEqual(rv.status_code, 200)
