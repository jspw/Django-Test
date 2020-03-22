from django  import forms
from django.core import validators


# custom validator for Name field that start with 'z'
def check_for_z(value):  # for 'value' django will detect it as a custom  validator 
    if(value[0].lower()!='z'):
        raise forms.ValidationError("Name need to start with 'z'")



class usersForm(forms.Form):
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)]) #this  is for bot
    
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again : ")
    location = forms.CharField()
    text =forms.CharField(widget=forms.Textarea)
    

    #validation custom for bots

    # def clearn_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0 :
    #         raise forms.ValidationError("Fuck You BOT")
    #     return botcatcher

    def clean(self):
        cleaned_data =super().clean()
        email = cleaned_data.get('email')
        vemail = cleaned_data.get('verify_email')

        if email!=vemail :
            raise forms.ValidationError("Make sure email match!") 