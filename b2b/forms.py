from models import *
from django.contrib.auth.forms import UserCreationForm


class b2bCForm(UserCreationForm):
    class Meta:
        model = Printer
        fields = ('username', 'password1', 'password2', 'name', 'email', 'address', 'phone', 'website', 'services',
                  'lat', 'lon', 'logo', 'categories', 'tags')

