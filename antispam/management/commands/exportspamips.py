import csv
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from antispam.models import SpamIP


class Command(BaseCommand):
    help = "Exports spam IP address into csv"

    def handle(self, *args, **kwargs):
        spam_ips = SpamIP.objects.all()
        file_path = os.path.join(settings.BASE_DIR, 'spamips.csv')
        with open(file_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            for ip in spam_ips:
                ip_list = [ip.ip_address, str(ip.created_on)]
                csvwriter.writerow(ip_list)
