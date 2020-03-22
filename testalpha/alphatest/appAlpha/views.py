from django.shortcuts import render
# from django.http import HttpRequest
from appAlpha.forms import newUser
from django  import forms
from django.core import validators
# from . import forms
# Create your views here.

def index(request):
    return render(request,'appAlpha/index.html')


def signup(request):

    form  = newUser()

    if(request.method == 'POST'):
        form = newUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else :
            forms.ValidationError("Invalid Input!")

    return render(request,'appAlpha/signup.html',{'form':form})

