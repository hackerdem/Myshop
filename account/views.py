from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.models import User
from .models import Profile
def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    

                    return HttpResponse('The account is done')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form=LoginForm()
        return render(request,'account/login.html',{'form':form})


def user_register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active=False
            new_user.save()
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form=UserRegistrationForm() 
    return render(request,'account/register.html',{'user_form':user_form})