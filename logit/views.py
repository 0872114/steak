from forms import MyUserCreationForm
from django.shortcuts import render_to_response


def login(request):
    form = MyUserCreationForm()
    return render_to_response('logit/login.html', {'form': form})


def register(request):
    form = MyUserCreationForm()
    return render_to_response("logit/register.html", {
        'form': form})
