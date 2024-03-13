from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

@login_required
def home (request):
    return render(request, 'login/registration.html')



def exit(request):
    logout(request)
    return redirect('/index')