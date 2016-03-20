from django.test import TestCase
from django.db import IntegrityError

from antispam.models import SpamIP


class SpamIPTestCase(TestCase):

    def test_spam_ip_create_update_delete(self):
        spam_ip = SpamIP.objects.create(ip_address='1.1.1.1')
        self.assertEqual(SpamIP.objects.filter(ip_address='1.1.1.1').exists(), True)

        spam_ip.ip_address = '2.2.2.2'
        spam_ip.save()
        self.assertEqual(SpamIP.objects.filter(ip_address='1.1.1.1').exists(), False)
        self.assertEqual(SpamIP.objects.filter(ip_address='2.2.2.2').exists(), True)

        spam_ip.delete()
        self.assertEqual(SpamIP.objects.filter(ip_address='2.2.2.2').exists(), False)

    def test_spam_ip_uniqueness(self):
        SpamIP.objects.create(ip_address='1.1.1.1')

        try:
            SpamIP.objects.create(ip_address='1.1.1.1')
            unique = False
        except IntegrityError:
            unique = True

        self.assertEqual(unique, True)
