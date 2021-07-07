from django.test import TestCase


class AddViewTest(TestCase):
    def test(self):
        pass
        response = self.client.post(
            '/add/',
            data={
                'number1': 10,
                'number2': 20
            }
        )
        assert response.status_code == 200
        assert response.json() == {'result': 30}
