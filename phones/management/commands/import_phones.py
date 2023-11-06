import csv

from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for any_phone in phones:
            phone = Phone(
                id=any_phone['id'],
                name=any_phone['name'],
                price=any_phone['price'],
                image=any_phone['image'],
                release_date=any_phone['release_date'],
                lte_exists=any_phone['lte_exists'],
            )
            phone.save()
