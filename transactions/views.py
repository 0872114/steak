from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm


def paypal_view(request):
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "1.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "http://127.0.0.1:8000/" + reverse('paypal-ipn'),
        "return_url": "http://127.0.0.1:8000/",
        "cancel_return": "http://127.0.0.1:8000/user/register/",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form' : form}
    return render_to_response('transactions/payment.html', context)


