from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name = models.CharField(max_length=50,blank=True,null=True)
    Email = models.EmailField(max_length=50,blank=True,null=True)
    Message = models.TextField(max_length=500,blank=True,null=True)

class CreateAccountDB(models.Model):
    First_Name = models.CharField(max_length=50,blank=True,null=True)
    Last_Name = models.CharField(max_length=50,blank=True,null=True)
    Username = models.CharField(max_length=50,blank=True,null=True)
    Email_Id = models.EmailField(max_length=50,blank=True,null=True)
    Password = models.CharField(max_length=50,blank=True,null=True)

class CartDB(models.Model):
    User_Name = models.CharField(max_length=50,null=True,blank=True)
    Product_Name = models.CharField(max_length=50,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)

class OrderDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,blank=True,null=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Address = models.TextField(max_length=500,null=True,blank=True)
    Country = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Message = models.TextField(max_length=500, null=True, blank=True)
    Total_Amount = models.IntegerField(null=True, blank=True)



