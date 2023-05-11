from unittest import TestCase


class TestUF(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        from app import create_app
        from config import config
        cls.app = create_app(config['test'])
        cls.client = cls.app.test_client()
        cls.routes = {
            'get_uf': '/api/v1/uf/',
        }
        return super().setUpClass()

    def test_get_uf(self):
        response = self.client.get(self.routes.get('get_uf') + '10-05-2022')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'UF value')
        self.assertIsNotNone(response.json['data'])

    def test_get_uf_invalid_date(self):
        response = self.client.get(self.routes.get('get_uf')+'45-13-2020')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid date')

    def test_get_uf_date_out_of_range(self):
        response = self.client.get(self.routes.get('get_uf')+'10-05-2000')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Date out of range')
