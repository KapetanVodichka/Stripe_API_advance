from django.contrib import admin

from stripe_app.models import Item, Order

admin.site.register(Item)

admin.site.register(Order)