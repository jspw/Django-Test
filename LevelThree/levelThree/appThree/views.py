from django.shortcuts import render
from django.http import HttpRequest
from . import forms 
from appThree.models import Users
# Create your views here.

def index(request):
    return render(request,'appThree/index.html')

def users(request):
    user = Users.objects.order_by('name')
    user_dict = {"user":user}
    return render(request,'appThree/users.html',context=user_dict)

def form(request):
    form = forms.usersForm(request.POST);

    if form.is_valid():
        print("Validation Success!")
        print("Name : " + form.cleaned_data['name'])
        print("Email : " + form.cleaned_data['email'])
        print("Location : " + form.cleaned_data['location'])
        # print(form.cleaned_data)


    
    return render(request,'appThree/form.html',{"form":form})