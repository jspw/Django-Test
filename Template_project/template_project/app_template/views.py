from django.shortcuts import render
from app_template.forms import signup
from django.core import validators
from django import forms

# Create your views here.

def index(request):
    return render(request,'app_template/index.html')

def basic(request):
    return render(request,'app_template/basic.html')

def other(request):
    return render(request,'app_template/other.html')

def relateive_template(request):
    return render(request,'app_template/relative_url_template.html')



def signupform(request):
    form = signup()

    if(request.method == 'POST'):
        form = signup(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else :
            raise forms.ValidationError("Invalid Input !")

    return render(request,'app_template/signup.html',{'form':form})