from django.shortcuts import render_to_response, redirect
from forms import MyUserCreationForm
from django.contrib import auth
from django.template.context_processors import csrf


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = MyUserCreationForm()
    if request.POST:
        newuser_form = MyUserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('registration/register.html', args)