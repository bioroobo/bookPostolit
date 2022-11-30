from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='User name')
    age = forms.IntegerField(label='User age')