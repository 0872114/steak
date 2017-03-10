from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'login/$', logit),
    url(r'register/$', register)
]
