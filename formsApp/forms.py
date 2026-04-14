from django import forms
from .models import Login

class Loginform(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']