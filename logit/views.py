from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response


def logit(request):
    return render_to_response('logit/login.html')


def register(request):
    form = UserCreationForm()
    return render_to_response("logit/register.html", {
        'form': form})
