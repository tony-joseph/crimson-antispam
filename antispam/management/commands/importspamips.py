import csv

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from antispam.models import SpamIP


class Command(BaseCommand):
    help = "Imports spam IP address from csv file into database"

    def add_arguments(self, parser):
        parser.add_argument('csv_files', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        inserted_count = 0
        skipped_count = 0

        for csv_file in kwargs['csv_files']:
            with open(csv_file, 'r') as file_handle:
                csv_reader = csv.reader(file_handle)
                for row in csv_reader:
                    try:
                        SpamIP.objects.create(
                            ip_address=row[0],
                            created_on=row[1],
                        )
                        inserted_count += 1
                    except IntegrityError:
                        skipped_count += 1

        self.stdout.write(self.style.SUCCESS('Inserted {} new ip addresses'.format(inserted_count)))
        self.stdout.write(self.style.WARNING('Skipped {} existing addresses'.format(skipped_count)))
