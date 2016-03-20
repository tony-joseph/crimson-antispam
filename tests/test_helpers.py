from django.test import TestCase

from antispam.models import SpamIP
from antispam import helpers


class SpamIPTestCase(TestCase):

    def setUp(self):
        self.spam_ip1 = SpamIP.objects.create(ip_address='1.1.1.1')
        self.spam_ip2 = SpamIP.objects.create(ip_address='1.1.1.2')

    def test_add_spam_ip_helper(self):
        helpers.add_spam_ip(ip_address='2.2.2.1')
        self.assertEqual(SpamIP.objects.filter(ip_address='2.2.2.1').exists(), True)

    def test_bulk_add_spam_ip_helper(self):
        ip_list = ['3.3.3.1', '3.3.3.2', '3.3.3.3']
        helpers.bulk_add_spam_ip(ip_address_list=ip_list)
        self.assertEqual(SpamIP.objects.filter(ip_address='3.3.3.1').exists(), True)
        self.assertEqual(SpamIP.objects.filter(ip_address='3.3.3.2').exists(), True)
        self.assertEqual(SpamIP.objects.filter(ip_address='3.3.3.3').exists(), True)

    def test_is_spam_ip_helper(self):
        self.assertEqual(helpers.is_spam_ip(ip_address=self.spam_ip1.ip_address), True)
        self.assertEqual(helpers.is_spam_ip(ip_address='4.4.4.1'), False)

    def test_remove_spam_ip_helper(self):
        helpers.remove_spam_ip(ip_address=self.spam_ip2.ip_address)
        self.assertEqual(helpers.is_spam_ip(ip_address=self.spam_ip2.ip_address), False)
