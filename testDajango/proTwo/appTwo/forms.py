from django import forms


class formName(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    text  =forms.CharField(widget=forms.Textarea)

