from django.urls import path
from .import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),
    path('register',views.register),
    path('user_home',views.user_home),
    path('shop_home',views.shop_home),
    path('add_product',views.add_product),
    path('edit_product/<id>',views.edit_product),
    path('delete_product/<id>',views.delete_product),
    path('bookings',views.bookings),
    path('view_product/<id>',views.view_product),
    path('contact',views.contact),
    path('add_cart/<pid>',views.add_cart),
    path('cart_display',views.cart_display),
    path('delete_cart/<id>',views.cart_delete),
    path('add_phone',views.add_phone),
    path('buy/<id>',views.buy_pro),
    path('about',views.about),  
    path('add_accessories',views.add_accessories),
    # path('view_booking',views.user_view_booking),
    path('order',views.bookings),
    path('cancel_order/<pid>',views.cancel_order),
    path('seller',views.seller),



]