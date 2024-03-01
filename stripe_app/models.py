from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Стоимость')
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD',
                                verbose_name='Валюта')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Товары', related_name='orders')
    total_price = models.IntegerField(default=0, verbose_name='Общая стоимость')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def calculate_total_price(self):
        total = sum(item.price for item in self.items.all())
        self.total_price = total
