from django.core.management.base import BaseCommand

from stripe_app.models import Item


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Item.objects.create(
            name='Ноутбук',
            description='Описание ноутбука ппррпрп',
            price=100,
            currency='USD'
        )

        Item.objects.create(
            name='Телефон сяоми 3310',
            description='Описание сяоми 3310 выфрщвгыфивд',
            price=200,
            currency='EUR'
        )
