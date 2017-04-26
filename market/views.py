#!python
# -*- coding: utf8 -*-

from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from django.utils import timezone

from b2b.models import Printer
from b2c.forms import *
from forms import *
from datetime import datetime
import pytz


def bidmarket(request):
    if request.user.id:
        args = {}
        args.update(csrf(request))
        if 'response_order' in request.POST:
            current = Order.objects.get(id=int(request.POST['response_order']))
            responder = Printer.objects.get(id=int(request.POST['responder']))
            if responder.sub_expires.astimezone(pytz.UTC) > pytz.utc.localize(datetime.now()):
                current.responses.add(responder)
            else:
                return render(request, 'please_subscribe.html')

        user = request.user.id
        try:
            printer_user = Printer.objects.get(user__id=user)
            args['printer_id'] = printer_user.id
        except AttributeError:
            return render(request, 'please_login.html')
        except Printer.DoesNotExist:
            return render(request, 'please_login.html')
        try:
            orders = Order.objects.filter(market=True).exclude(user__isnull=True).order_by('datetime').reverse()[:100]
        except Order.DoesNotExist:
            return render(request, 'please_login.html')
        list = prepare_orders(orders)
        args['orders'] = list
        args['is_printer'] = True
        args['page'] = 'market_orders'
        return render(request, 'market/market.html', args)
    else:
        return render(request, 'please_login.html')


def received_orders(request):
    if request.user.id:
        orders = Order.objects.filter(destination__user_id=request.user.id).order_by('datetime').reverse()
        list = prepare_orders(orders)
        return render(request, 'market/received_orders.html',
                      {'orders': list, 'id': request.user.id, 'is_printer': True, 'page': 'my_orders'})
    else:
        return render(request, 'please_login.html')


def show_order(request, id=None):
    if id is None:
        return redirect('./')
    else:
        args = {}
        if request.user.id:
            user = request.user.id
            # If comment added
            if 'comment' in request.POST:
                sender = Printer.objects.get(id=int(request.POST['sender']))
                if sender.sub_expires and sender.sub_expires.astimezone(pytz.UTC) > pytz.utc.localize(datetime.now()):
                    form = MarketCommentForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('market_order', id=id)

                else:
                    return render(request, 'please_subscribe.html')

            # If response added
            elif 'response_order' in request.POST:
                current = Order.objects.get(id=int(request.POST['response_order']))
                responder = Printer.objects.get(id=int(request.POST['responder']))
                if responder.sub_expires and responder.sub_expires.astimezone(pytz.UTC) > pytz.utc.localize(datetime.now()):
                    current.responses.add(responder)
                else:
                    return render(request, 'please_subscribe.html')

            # If status changed
            elif 'status' in request.POST:
                instance = Order.objects.get(id=int(id))
                form = StatusForm(request.POST, instance=instance)
                if form.is_valid():
                    form.save()
                    return redirect('market_order', id=id)

            # Find out if an order exists
            try:
                order = Order.objects.get(id=int(id))
                # If current user got this order
                try:
                    if order.destination.user.id == user:
                        args['select'] = StatusForm(request.POST or None, instance=order)
                except AttributeError:
                    pass
                args['comments'] = []
                # Find current user's typography
                try:
                    printer_user = Printer.objects.get(user__id=user)
                    args['printer'] = dict(
                        id=printer_user.id,
                        user_id=printer_user.user.id,
                        name=printer_user.name
                    )
                except AttributeError:
                    return render(request, 'please_login.html')

                except Printer.DoesNotExist:
                    return render(request, 'please_login.html')

                # Get comments
                comments = MarketComment.objects.filter(order__id=int(id)).order_by('datetime')
                for comment in comments:
                    comment_data = dict(
                        id=comment.id,
                        datetime=comment.datetime,
                        comment=comment.comment,
                        sender=comment.sender,
                        sender_id=comment.sender.id,
                    )
                    args['comments'].append(comment_data)
                tuple(args['comments'])
                args.update(csrf(request))
                order_sorted = sort_order(order)
                args['order'] = order_sorted
                args['form'] = MarketCommentForm
                args['is_printer'] = True
                args['page'] = 'market_order'
                return render(request, 'market/show_order.html', args)

            except Order.DoesNotExist:
                return render(request, 'market/show_order.html',
                              {'error': 'DoesNotExist: matching order does not exist'})

        else:
            return render(request, 'please_login.html')


def private_all(request):
    if request.user.id:
        orders = Order.objects.filter(user_id=request.user.id).order_by('datetime').reverse()
        list = prepare_orders(orders)
        return render(request, 'market/received_orders.html',
                      {'orders': list, 'id': request.user.id, 'private': True, 'page': 'private_all', 'is_printer': False})

    else:
        return render(request, 'please_login.html')


def private_one(request, id=None):
    if id is None:
        return redirect('./')

    else:
        if 'destination' in request.POST:
            instance = Order.objects.get(id=int(id))
            form = SetDestinationForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('private_one', id=id)

        if request.user.id:
            # If order exists
            try:
                order = Order.objects.get(id=int(id))
                # if user is the creator
                if order.user.id == request.user.id:
                    args = {'is_private': True}
                    order_sorted = sort_order(order)
                    args['order'] = order_sorted
                    args['comments'] = []
                    # Get comments
                    comments = MarketComment.objects.filter(order__id=int(id)).order_by('datetime')
                    for comment in comments:
                        comment_data = dict(
                            id=comment.id,
                            datetime=comment.datetime,
                            comment=comment.comment,
                            sender=comment.sender,
                            sender_id=comment.sender.id,
                        )
                        args['comments'].append(comment_data)
                    tuple(args['comments'])
                    args.update(csrf(request))
                    args['destination'] = SetDestinationForm(instance=order)
                    args['page'] = 'private_one'
                    try:
                        args['destination_id'] = order.destination.id
                    except AttributeError:
                        pass
                    return render(request, 'market/show_order.html', args)

                else:
                    return render(request, 'please_login.html')

            except Order.DoesNotExist:
                return render(request, 'market/show_order.html',
                              {'error': 'DoesNotExist: matching order does not exist'})

        else:
            return render(request, 'please_login.html')


def sort_order(order):
    now = timezone.now()
    order_data = dict(
        id=order.id,
        market=order.market,
        status=order.get_status_display(),
        email=order.email,
        phone=order.phone,
        datetime=order.datetime,
        sender=order.sender,
        user=order.user,
        service=order.service,
        comment=order.comment,
        destination=order.destination,
    )
    # Get the tuple of respondents
    responses = order.responses.values()
    order_data['responses'] = {}
    for response in responses:
        order_data['responses'][response['id']] = response

    # Find out if order.destination.id exists (if an order is taken)
    try:
        order.destination.id
        order_data['taken'] = 1
    except AttributeError:
        order_data['taken'] = 0

    # Count full hours between now and when the order was created
    time_diff_hours = divmod((now - order.datetime).total_seconds(), 3600)[0]

    # Mark 3+ hours old unprocessed orders red, the new ones green,
    if order.status == 'new':
        if time_diff_hours >= 3:
            order_data['tr_class'] = 'tr-market-red'
        else:
            order_data['tr_class'] = 'tr-market-green'
    return order_data


def prepare_orders(orders):
    list = []

    for order in orders:
        order_data = sort_order(order)
        list.append(order_data)
    tuple(list)  # Tuples weigh less and process faster then lists
    return list
