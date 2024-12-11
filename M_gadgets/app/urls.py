from django.urls import path
from .import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),
    path('register',views.register),
]