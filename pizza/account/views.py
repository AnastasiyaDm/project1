from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from account.forms import CustomerRegForm as RegForm
from jsonview.decorators import json_view
from django.contrib.auth import authenticate, login as l, logout
# Create your views here.


@json_view
def alogin(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        l(request, user)
        return { 'status': 0, 'message': 'Welcome!!!!' }
    else:
        return { 'status': 1, 'message': 'Login or password incorrect!!!' }




def login(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        l(request, user)
        return redirect('home')
    else:
        messages.warning(request, 'Need to register')
        return redirect('home')




def logoutme(request):
    logout(request)
    return redirect('home')

def registration(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #username = form.cleaned_data['username']
            user = form.save()
            messages.success(request, 'You are registered, %s!' % user.id)
            return redirect('home')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = RegForm()
