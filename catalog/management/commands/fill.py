from django.core.management import BaseCommand
import json
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()

        with open('data.json') as file:
            data = json.load(file)

        product_for_create = []
        for item in data:
            product = item['fields']
            product_for_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(product_for_create)
