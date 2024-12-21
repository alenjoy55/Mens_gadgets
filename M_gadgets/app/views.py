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
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    else:
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
                    req.session['shop']=uname
                    return redirect(shop_home)
                else:
                    req.session['user']=uname
                    return redirect(user_home)
            else:
                messages.warning(req, "invaild uname or password")
            return redirect(shop_login)
        else:
            return render(req,'login.html')
def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)

def register(req):
    if req.method=='POST':
        name=req.POST['uname']
        email=req.POST['email']
        password=req.POST['password']
        # send_mail('e_shop registration', 'e_shop account created', settings.EMAIL_HOST_USER, [email])

        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
            return redirect(shop_login)
        except:
                messages.warning(req, "user already exists")
                return redirect(register)

    else:
        return render(req,'register.html')
    
def about(req):
    return render(req,'about.html')

# ------------admin---------------------------  
def shop_home(req):
    if 'shop' in req.session:
        product=Product.objects.all()
        return render(req,'shop/shop_home.html',{'products':product})
    else:
        return render(shop_login)
    # return render(req,'shop/shop_home.html')

def add_product(req):
    if req.method=='POST':
        id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        description=req.POST['description']
        # highlight=req.POST['highlight']
        offer_price=req.POST['offer_price']
        file=req.FILES['img']
        data=Product.objects.create(product_id=id,name=name,price=price,description=description,offer_price=offer_price,img=file)
        data.save()
    return render(req,'shop/add_product.html')

def edit_product(req,id):
    Pro=Product.objects.get(pk=id)
    if req.method=='POST':
        e_id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        description=req.POST['description']
        offer_price=req.POST['offer_price']
        img=req.FILES.get('img')
        # print(file)
        if img:
            Product.objects.filter(pk=id).update(product_id=e_id,name=name,price=price,description=description,offer_price=offer_price,)
            data=Product.objects.get(pk=id)
            data.img=img
            data.save()
        else:
            Product.objects.filter(pk=id).update(product_id=e_id,name=name,price=price,description=description,offer_price=offer_price)
            return redirect(shop_home)
    return render(req,'shop/edit_product.html',{'data':Pro})

def delete_product(req,id):
    data=Product.objects.get(pk=id)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)

def bookings(req):
       bookings=Buy.objects.all()[::-1][:2]
       print(bookings)
       return render(req,'shop/bookings.html',{'data':bookings})
def add_phone(req):
    if 'shop' in req.session:
        if req.method=='POST':
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            specifications=req.POST['specifications']
            img=req.FILES['img']
            phone=Phone(name=name,price=price,offer_price=offer_price,
                        specifications=specifications,img=img)
            phone.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_phone.html')
    else:
        return redirect(shop_login)
def add_accessories(req):
    return render(req,'shop/accessories.html')
# ------------user-----------------------
def user_home(req):
    if 'user' in req.session:
        product=Product.objects.all()
        return render(req,'user/user_home.html',{'products':product})
    # return render(req,'user/user_home.html')

# def view_product(req,pid):
#     if 'user' in req.session:
#         data=Product.objects.get(pk=pid)
#         return render(req,'user/view_product.html',{'product': data})
#     else:
#         return render(req,'user/home.html')
    
def view_product(req,id):
    log_user=User.objects.get(username=req.session['user'])
    product=Product.objects.get(pk=id)
    try:
        cart=Cart.objects.get(product=product,user=log_user)
    except:
        cart=None
    return render(req,'user/view_product.html',{'product':product,'cart':cart})


# def view_product(req,id):
#     log_user=User.objects.get(username=req.session['user'])
#     product=Product.objects.get(pk=id)
#     try:
#         cart=Cart.objects.get(product=product,user=log_user)
#     except:
#         cart=None
#     return render(req,'user/view_pro.html',{'product':product,'cart':cart})
    # return render(req,'user/view_product.html')

def add_cart(req,pid):
    Products=Product.objects.get(pk=pid)
    print(Products)
    user=User.objects.get(username=req.session['user'])
    print(user)
    data=Cart.objects.create(user=user,product=Products)
    data.save()
    return redirect(cart_display)

def cart_display(req):
    log_user=User.objects.get(username=req.session['user'])
    data=Cart.objects.filter(user=log_user)
    return render(req,'user/cart_display.html',{'data':data})

def cart_delete(req,id):
    data=Cart.objects.get(pk=id)
    data.delete()
    return redirect(cart_display)

def contact(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        message = req.POST['message']
        try:
            data = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            data.save()
            return render(req, 'user/contact.html')
        except Exception as e:
            return render(req,'user/contact.html')
    
    return render(req,'user/contact.html')
def buy_pro(req,id):
    product=Product.objects.get(pk=id)
    user=User.objects.get(username=req.session['user'])
    price=product.offer_price
    data=Buy.objects.create(user=user,product=product,price=price)
    data.save()
    return redirect(user_home)

def user_view_booking(req):
    user=User.objects.get(username=req.session['user'])
    data=Buy.objects.filter(user=user)
    return render(req,'user/view_booking.html',{'data':data})


def add_accessories(req):
    if 'shop' in req.session:
        if req.method=='POST':
            accessory_id=req.POST['accessory_id']
            name=req.POST['name']
            brand=req.POST['brand']
            color=req.POST['color']
            description=req.POST['description']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            stock=req.POST['stock']
            warranty=req.POST['warranty']
            img=req.FILES['img']
            accessory=Accessories(accessory_id=accessory_id,name=name,brand=brand,color=color,
                                  description=description,price=price,offer_price=offer_price,
                                  stock=stock,warranty=warranty,img=img)
            accessory.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_accessories.html')
    else:
        return redirect(shop_login)