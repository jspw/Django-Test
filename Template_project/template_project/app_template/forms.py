from django  import forms
from app_template.models import Users

class signup(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'