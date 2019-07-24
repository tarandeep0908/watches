from django.db import models
from django.contrib.auth.forms import User

class Category(models.Model):
    cname=models.CharField(max_length=30)
    def __str__(self):
        return self.cname
    
class Product(models.Model):
    Name=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete='CASCADE',default=None)
    Price=models.IntegerField()
    Band_color=models.CharField(max_length=20)
    Band_material=models.CharField(max_length=20)
    Brand=models.CharField(max_length=20)
    Collection=models.CharField(max_length=20)
    Dial_color=models.CharField(max_length=20)
    Crystal=models.CharField(max_length=20)
    Display_type=models.CharField(max_length=20)
    Case_Shape=models.CharField(max_length=20)
    Model_Number=models.CharField(max_length=20)
    Part_Number=models.CharField(max_length=20)
    Special_Features=models.CharField(max_length=20)
    Warranty_Type=models.CharField(max_length=20)
    Movement=models.CharField(max_length=20)
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images', default=None)
    img3 = models.ImageField(upload_to='images', default=None)
    img4 = models.ImageField(upload_to='images', default=None)
    img5 = models.ImageField(upload_to='images', default=None)
    img6 = models.ImageField(upload_to='images', default=None)
    img7 = models.ImageField(upload_to='images', default=None)

class Cart(models.Model):
    cart_user=models.ForeignKey(User,on_delete='CASCADE',default=None)
    cart_product=models.ForeignKey(Product,on_delete='CASCADE',default=None)
    count=models.IntegerField()
    total=models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.cart_user)

class Checkout(models.Model):
    chname=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=50)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)

    def __str__(self):
        return self.chname
