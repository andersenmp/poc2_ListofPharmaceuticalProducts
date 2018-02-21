from django.test import TestCase
from django.test import Client
from django.urls import reverse

class TestHomeView(TestCase):
    # def setUp(self):
    #     user = User.objects.create_user('temp', 'temp@gmail.com', 'temp')

    def test_view_without_auth(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        response_content = str(response.content, encoding='utf8')
        self.assertIn('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', response_content)










