from django.test import TestCase
from django.test import Client
from django.urls import reverse

class TestHomeView(TestCase):
    # def setUp(self):
    #     user = User.objects.create_user('temp', 'temp@gmail.com', 'temp')

    def test_view_without_auth(self):
        url = reverse('ListofPharmaceuticalProducts:home')
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        response_content = str(response.content, encoding='utf8')
        self.assertIn('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', response_content)


class TestGetMedicalListView(TestCase):
    # def setUp(self):
    #     user = User.objects.create_user('temp', 'temp@gmail.com', 'temp')

    def test_view_get(self):
        url = reverse('ListofPharmaceuticalProducts:GetMedicalListView')
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_view_post_without_csrf(self):
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse('ListofPharmaceuticalProducts:GetMedicalListView'))
        self.assertEqual(response.status_code, 403)

    def test_view_post(self):
        url = reverse('ListofPharmaceuticalProducts:GetMedicalListView')
        client = Client()
        response = client.post(url)
        self.assertEqual(response.status_code, 200)
        response_content = str(response.content, encoding='utf8')
        self.assertJSONEqual(response_content, {'results': [], 'total': 0})




