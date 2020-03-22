from django import forms
from django.core import validators
from appAlpha.models import Users


# def usernameValid(value):
#     print(value[0])
#     if(value[0].lower()!='s'):
#         raise forms.ValidationError("username should start with 's' !")

# class userForm(forms.Form):
#     first_name = forms.CharField(label="Enter First Name")
#     last_name = forms.CharField(label="Enter Last Name")
#     username = forms.CharField(validators=[usernameValid],label="Enter Username")
#     email = forms.EmailField()
#     passwd = forms.CharField(label="Enter password")
#     vpasswd = forms.CharField(label="Enter password again")


#     def clean(self):
#         clean_data = super().clean()
#         passw = clean_data.get('passwd')
#         vpasswd = clean_data.get('vpasswd')

#         if(passw != vpasswd):
#             raise forms.ValidationError("Make sure your passwords match!")



class newUser(forms.ModelForm):
    class Meta():
        model = Users
        fields='__all__' 