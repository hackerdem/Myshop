from django import forms
from .models import User
from django.contrib import admin


from django.contrib.auth.forms import ReadOnlyPasswordHashField
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('email','first_name')
  
    def clean_password2(self):
        cd=self.cleaned_data
        password=cd['password']
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        if len(password)<=7 or password.islower() or password.isdigit() or password.isupper():
            raise forms.ValidationError('Password should be at least 8 characters and consist of numbers,upper and lower case characters.')
        return cd['password2']

    def save(self,commit=True):
        user=super(UserRegistrationForm,self).save(commit=False)
        user.set_password=(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        mudel=User
        fields=('email','first_name','password',)
    def clean_password(self):
        return self.initial["password"]
