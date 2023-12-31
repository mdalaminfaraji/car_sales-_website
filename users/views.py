from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from cars.models import Order
def register(request):
    if request.method=="POST":
        register_form=forms.SignUpForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Register successfully done')
            return redirect('register')
    else:
        register_form = forms.SignUpForm()
    return render(request, 'register.html', {'form':register_form, 'type':'Register'})


def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Login successfully done')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'user do not find please  login')
                return  redirect('register')
          
    else:
        form=AuthenticationForm()
        return render(request, 'register.html', {'form':form, 'type':'login'})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
        user=request.user
        orders=Order.objects.filter(user=user)
        for car in orders:
                print(car)
        return render(request, 'profile.html', {"data":request.user, "orders":orders})

@login_required
def edit_profile(request):
    if request.method=="POST":
        profile_form=forms.ChangeUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully done')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserData( instance=request.user)
    return render(request, 'update_profile.html', {'form':profile_form, 'type':'Profile', "user":request.user})



