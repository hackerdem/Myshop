from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.models import User
from .models import Profile,UserActivation
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.tokens import default_token_generator
from datetime import datetime

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('http://arts.com:8000/')
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
            uid=urlsafe_base64_encode(force_bytes(new_user.pk)).decode()
            token=default_token_generator.make_token(new_user)
             
            current_site = get_current_site(request)
            mail_subject = 'Activate your artsshop account.'
            print(uid,token)
            message = render_to_string('account/confirmation_mail.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid':uid,
                'token':token,
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            new_user.save()
            UserActivation.objects.create(user=new_user, access_token=token)
            return render(request,'account/register_done.html',{'new_user':new_user,'uid':uid,'token':token})
    else:
        user_form=UserRegistrationForm() 
    return render(request,'account/register.html',{'user_form':user_form})

def user_logout(request):
    logout(request)
    return HttpResponse(product_list(request)) #Fix this later

def activate(request, uidb64, token):
    
    try:
        print("mmm",uidb64)
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print("mmm",uid,user,user.id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    check_user= UserActivation.objects.get(user='erdemo')
    if check_user and check_user.access_token==token:
        user.is_active = True
        user.save()
        login(request, user)# delete this later
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')