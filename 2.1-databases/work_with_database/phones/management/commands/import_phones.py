import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'импорт данных csv'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path',
            type=str,
            nargs='?',
            default='phones.csv',
            help='путь к csv'
        )

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                name = phone['name']
                price = float(phone['price'])
                image = phone['image']
                release_date = phone['release_date']
                lte_exists = phone['lte_exists'].lower() == 'true'
                slug = slugify(name)

                phone_obj, created = Phone.objects.get_or_create(
                    name=name,
                    defaults={
                        'price': price,
                        'image': image,
                        'release_date': release_date,
                        'lte_exists': lte_exists,
                        'slug': slug,
                    }
                )


