#! python
# -- coding: utf-8 ---


from django.shortcuts import render_to_response, redirect
from models import Entry

def main_page(request, titles=u'Главная'):
    contents = Entry.objects.get(title=titles).short_text
    context = {'short_text' :  contents, 'title' : titles}
    return render_to_response('content/main_page.html', context)

def about(request):
    return main_page(request, titles=u'О нас')

def printing1(request):
    return main_page(request, titles=u'О печати 1')

def printing2(request):
    return main_page(request, titles=u'О печати 2')

def printing3(request):
    return main_page(request, titles=u'О печати 3')