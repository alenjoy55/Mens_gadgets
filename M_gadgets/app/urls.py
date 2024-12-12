from django.urls import path
from .import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),
    path('register',views.register),
    path('user_home',views.user_home),
    path('shop_home',views.shop_home),
]