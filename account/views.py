from .forms import SignupForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from PIL import Image
import qrcode
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserLink
# Create your views here.

# index view


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/profile/')

# register view


def sign_up(request):
    if request.method == 'POST':
        fs = SignupForm(request.POST)
        if fs.is_valid():
            messages.success(request, 'Account created successfullly ')
            fs.save()
    else:
        fs = SignupForm()
    return render(request, 'signup.html', {'form': fs})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fl = AuthenticationForm(request=request, data=request.POST)
            if fl.is_valid():
                uname = fl.cleaned_data['username']
                upass = fl.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You login Successfully  ')
                    return HttpResponseRedirect('/profile/')
                    # return render(request, 'Qrcode/profile.html', {'user': user})
        else:
            fl = AuthenticationForm()
        return render(request, 'login.html', {'form': fl})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fp = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fp = EditUserProfileForm(request.POST, instance=request.user)
                users = None
            if fp.is_valid():
                messages.success(request, 'Profile Update !!  ')
                fp.save()
        else:
            if request.user.is_superuser == True:
                fp = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fp = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'profile.html', {'name': request.user.username, 'form': fp, 'users': users})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fc = PasswordChangeForm(user=request.user, data=request.POST)
            if fc.is_valid():
                fc.save()
                update_session_auth_hash(request, fc.user)
                messages.success(request, 'Password Change Suceesfuuly !!')
                return HttpResponseRedirect('/profile/')
        else:
            fc = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form': fc})
    else:
        return HttpResponseRedirect('/profile/')


def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fu = EditAdminProfileForm(instance=pi)
        return render(request, 'userdetail.html', {'form': fu})
    else:
        return HttpResponseRedirect('/login/')


def user_dash(request):
    if request.user.is_authenticated:
        prev = UserLink.objects.all()
        return render(request, 'dash.html')


data = None
title = None


def qr_code(request):
    global data
    global title
    if request.user.is_authenticated:
        if request.method == 'POST':
            qr = qrcode.QRCode(version=1,
                               box_size=10,
                               border=5)
            data = request.POST['data']
            title = request.POST['title']
            qr.add_data(data)
            img = qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")
            img.save("account/static/account/img/test.png")
            fq = UserLink(username=str(request.user),
                          qr_link=data, qr_title=title)
            fq.save()
        else:
            pass
        return render(request, "dash.html", {'data': data, 'title': title})
    else:
        return HttpResponseRedirect('/login/')


def user_histroy(request):
    if request.user.is_authenticated:
        prev1 = UserLink.objects.filter(username=str(request.user))
        prev = prev1
        return render(request, 'view_history.html', {'pre': prev})
