from django import forms

class LoginForm(forms.Form):
    account = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    account = forms.CharField()
    password = forms.CharField()

    nickname = forms.CharField()
    email = forms.EmailField()

    sex = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField()
