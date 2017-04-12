#!python
# -*- coding: utf8 -*-

""" Адреса уровня проекта

grill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sample/', include('sample.urls')),
    url(r'^', include('b2c.urls')),
    url(r'^user/', include('logit.urls')),
    url(r'^user/', include('django.contrib.auth.urls'), name="login"),
    url(r'', include('content.urls')),
    url(r'^redactor', include('redactor.urls')),
    url(r'^paypal', include('paypal.standard.ipn.urls')),
    url(r'^paytest/', include('transactions.urls')),
    url(r'^market/', include('market.urls')),
    url(r'^b2b/', include('b2b.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^accounts/', include('account.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
