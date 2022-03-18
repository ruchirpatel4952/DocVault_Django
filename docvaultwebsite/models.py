from django.db import models

class user_details(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=130)
    confirm_password = models.CharField(default="",max_length=130)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    dob = models.DateField(default="2000-01-01")
    address = models.TextField(default="Address")
    city = models.CharField(max_length=30,default='City')
    state = models.CharField(max_length=30, default='State')
    dp = models.ImageField(upload_to='dp_folder', default="dp_folder/defaultuser.jpg")
    role = models.IntegerField(default="2")
    status = models.IntegerField(default="1")


class contact_us(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.TextField()
