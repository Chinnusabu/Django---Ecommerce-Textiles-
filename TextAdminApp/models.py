from django.db import models

# Create your models here.
class addcat(models.Model):
    Category = models.CharField(max_length=50,null=True,blank=True)
    Description = models.TextField(max_length=1000,null=True,blank=True)
    Image = models.ImageField(upload_to='Category_Pictures')
class ProductDB(models.Model):
    Category_Name = models.CharField(max_length=50,null=True,blank=True)
    Product = models.CharField(max_length=50,null=True,blank=True)
    Pr_Description = models.TextField(max_length=5000,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Brand = models.CharField(max_length=50,null=True,blank=True)
    Pr_Image1 = models.ImageField(upload_to='Product Images',null=True,blank=True)
    Pr_Image2 = models.ImageField(upload_to='Product Images',null=True,blank=True)
    Pr_Image3 = models.ImageField(upload_to='Product Images',null=True,blank=True)

