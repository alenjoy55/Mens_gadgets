from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    product_id=models.TextField()
    name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    description=models.TextField()
    # highlight=models.TextField()
    img=models.FileField()

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)

class Contact(models.Model):
    name=models.TextField()
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()

class Phone(models.Model):
    # brand = models.TextField()
    name = models.TextField()
    price = models.IntegerField()
    offer_price = models.IntegerField()
    specifications = models.TextField(default="Not specified")
    img=models.FileField()

class Accessories(models.Model):
    accessory_id = models.TextField()
    name = models.TextField()           
    brand = models.TextField()                
    description = models.TextField()                  
    price = models.IntegerField()
    offer_price = models.IntegerField()
    color = models.TextField()
    stock = models.IntegerField()
    warranty = models.TextField()
    img=models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
