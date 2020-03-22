from django.shortcuts import render
from appTwo.models import User
from . import forms #import from the same folder (.)

# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'appTwo/users.html',context=user_dict)

def form_name_view(request):
    form = forms.formName();
    return render(request,'appTwo/form_page.html',{'form':form})