from django.test import TestCase, Client
from django.urls import reverse

from antispam.models import SpamIP


class DecoratorTestCase(TestCase):

    def test_block_spam_ip_decorator(self):
        client = Client()
        response = client.get(reverse('blocked_by_decorator'))
        self.assertEqual(response.status_code, 200)
        SpamIP.objects.create(ip_address='127.0.0.1')
        response = client.get(reverse('blocked_by_decorator'))
        self.assertEqual(response.status_code, 403)
