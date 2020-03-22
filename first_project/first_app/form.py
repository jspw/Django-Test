from django  import forms

class usersForm(forms.Form):
    name = forms.CharField()
    emali = forms.EmailField()
    location = forms.CharField()

