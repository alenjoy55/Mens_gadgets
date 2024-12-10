from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def shop_login(req):
    return render(req,'login.html')
        
def shop_home(req):
     return render(req,'shop/shop_home.html')


def user_home(req):
    return render(req,'user/user_home.html')
