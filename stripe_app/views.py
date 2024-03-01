from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import stripe
from django.conf import settings

from stripe_app.models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_stripe_session(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('stripe_app:item_page', kwargs={'item_id': item_id})),
            cancel_url=request.build_absolute_uri(reverse('stripe_app:item_page', kwargs={'item_id': item_id})),
        )
        return JsonResponse({'session_id': session.id})
    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_item_page(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'currency': item.currency,
    }
    return render(request, 'stripe_app/item_page.html', context)


def create_order(request):
    if request.method == 'POST':
        items_ids = request.POST.getlist('items')
        items = Item.objects.filter(pk__in=items_ids)
        order = Order.objects.create()
        order.items.add(*items)

        order.calculate_total_price()
        order.save()

        return redirect('stripe_app:order_page', order_id=order.id)
    else:
        items = Item.objects.all()
        return render(request, 'stripe_app/order_form.html', {'items': items})


def get_stripe_session_for_order(request, order_id):
    order = Order.objects.get(id=order_id)
    total_price = order.total_price

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Order',
                },
                'unit_amount': total_price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('stripe_app:order_page', kwargs={'order_id': order_id})),
        cancel_url=request.build_absolute_uri(reverse('stripe_app:order_page', kwargs={'order_id': order_id})),
    )

    return JsonResponse({'session_id': session.id})


def get_order_page(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'stripe_app/order_page.html', context)
