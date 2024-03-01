from django.urls import path

from stripe_app.apps import StripeAppConfig
from stripe_app.views import get_stripe_session, get_item_page, create_order, get_stripe_session_for_order, \
    get_order_page

app_name = StripeAppConfig.name

urlpatterns = [
    # Получение StripeSession и осуществление CheckoutSession для Item
    path('buy/<int:item_id>/', get_stripe_session, name='get_session'),
    path('item/<int:item_id>/', get_item_page, name='item_page'),

    # Создание Order путём сбора корзины из существующих Item
    path('create_order/', create_order, name='create_order'),

    # Получение StripeSession и осуществление CheckoutSession для Order
    path('order/<int:order_id>/', get_order_page, name='order_page'),
    path('buy_order/<int:order_id>/', get_stripe_session_for_order, name='get_session_for_order'),
]
