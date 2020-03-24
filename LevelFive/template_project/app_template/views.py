from django.shortcuts import render
from app_template.forms import UserProfileInfoForm,UserForm
from django.core import validators
from django import forms


#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse 
# from django.core.urlresolvers import reverse  #django 2 removes urlresolvers
from django.urls import reverse

from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    contest_dict = {'text':"Hello world!"}
    return render(request,'app_template/index.html',contest_dict)

@login_required
def special(request):
    return HttpResponse("You are loggedin , Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def basic(request):
    return render(request,'app_template/basic.html')

def other(request):
    return render(request,'app_template/other.html')

def relateive_template(request):
    return render(
            request,
            'app_template/relative_url_template.html'
        )



def signupform(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  #hashing the password
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user



            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()


            registered = True


        else :
             print(user_form.errors,profile_form.errors)

    else :
        user_form  = UserForm()

        profile_form = UserProfileInfoForm()


    return render(
            request,
            'app_template/signup.html',
                {
                    'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered,
                }
        )



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username = username,password=password)

        if user :
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))

            else :
                return HttpResponse("Account is not Active")


        else :
            print("Someone tried to login and failed")

            print("Username : {} and password {}".format(username,password))


            return HttpResponse("Invalid login detailed supplied")


    else :
        return render(request,'app_template/login.html')

