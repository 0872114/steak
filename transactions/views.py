from django.core.urlresolvers import reverse
from b2b.models import Printer
from datetime import datetime, timedelta
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from django.shortcuts import render
from paypal.standard.ipn.signals import *
from models import Superuser
import pytz


def paypal_view(request):
    money_reciever = Superuser.objects.first()
    paypal_dict = {
        "business": money_reciever.reciever,
        "currency_code": "RUB",
        "amount": money_reciever.amout,
        "item_name": "Subscription",
        "invoice": "unique-invoice-id",
        "notify_url": "http://127.0.0.1:8000/" + reverse('paypal-ipn'),
        "return_url": "http://127.0.0.1:8000/",
        "cancel_return": "http://127.0.0.1:8000/user/register/",
        "custom": request.user.id,
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form' : form}
    valid_ipn_received.connect(show_me_the_money)
    return render(request,'transactions/payment.html', context)



def show_me_the_money(sender,request, **kwargs):
        money_reciever = Superuser.objects.first()
        ipn_obj = sender
        if ipn_obj.payment_status == ST_PP_COMPLETED:
            if ipn_obj.receiver_email != money_reciever.reciever:
                # Not a valid payment
                return render(request, 'transactions/invalid.html')
            if ipn_obj.amount != money_reciever.amount:
                return render(request, 'transactions/invalid.html')
            if ipn_obj.custom == request.user.id:
                instance = Printer.objects.get(id=request.user.id)
                if instance.sub_expires.astimezone(pytz.UTC) < pytz.utc.localize(datetime.now()):
                    instance.sub_expires = datetime.now() + timedelta(days=30)
                else:
                    instance.sub_expires += timedelta(days=30)
                instance.subscribed = True
                instance.save()
                return render(request, 'transactions/valid.html')
        else:
            return render(request, 'transactions/invalid.html')