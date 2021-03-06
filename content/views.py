#! python
# -- coding: utf-8 ---

from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from models import Entry
from django.shortcuts import render

def main_page(request, titles=u'Главная'):
    try:
        contents = Entry.objects.get(title=titles).short_text
    except Entry.DoesNotExist:
        return redirect('map')
    context = {'short_text' :  contents, 'title' : titles}
    return render(request, 'content/main_page.html', context)

def about(request):
    return main_page(request, titles=u'О нас')

def printing1(request):
    return main_page(request, titles=u'О печати 1')

def printing2(request):
    return main_page(request, titles=u'О печати 2')

def printing3(request):
    return main_page(request, titles=u'О печати 3')

def logout_view(request):
  auth.logout(request)
  # Redirect to a success page.
  return main_page(request, titles=u'Главная')