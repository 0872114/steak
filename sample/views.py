#!python
# -*- coding: utf8 -*-

from django.shortcuts import render

def home(request):
    """Банально цепляем шаблон
    """
    return render(request,"sample/home.html")