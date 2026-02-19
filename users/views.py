from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def login(request):
    error = False

    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
    context = {'form': form, 'error': error}
    return render(request, 'users/login.html', context)