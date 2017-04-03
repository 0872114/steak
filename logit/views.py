from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.context_processors import csrf

from forms import MyUserCreationForm


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = MyUserCreationForm()
    if request.POST:
        newuser_form = MyUserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(
                username=newuser_form.cleaned_data['username'],
                password=newuser_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'registration/register.html', args)
