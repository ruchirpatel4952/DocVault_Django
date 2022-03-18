from django.db import models

# Create your models here.
from docvaultwebsite.models import user_details


class security_technique(models.Model):
    security_name = models.CharField(max_length=30)

    def __str__(self):
        return self.security_name


class document_details(models.Model):
    login_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=30)
    document_security_technique = models.ForeignKey(security_technique, on_delete=models.CASCADE)
    document_title = models.CharField(max_length=30)
    document_description = models.TextField(default="")
    document_status = models.CharField(max_length=30)
    document_size = models.CharField(max_length=50)
    document = models.FileField(upload_to='document_folder')
    document_publish_date_time = models.DateField(auto_now_add=True, editable=False)
    document_password = models.CharField(max_length=30)
    document_bin = models.IntegerField(default=0)
    document_sent = models.IntegerField(default=0)


class document_privilege(models.Model):
    login_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    document_id = models.ForeignKey(document_details, on_delete=models.CASCADE)
    privilege_status = models.IntegerField()
    sent_to = models.CharField(max_length=30,default="")


class feedback(models.Model):
    login_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default="")
    lastname = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=30, default="")
    feedback_comment = models.TextField()


class premium_package(models.Model):
    package_type = models.CharField(max_length=30)
    package_publish_date_time = models.DateTimeField(auto_now_add=True, editable=False)
    package_status = models.CharField(max_length=30)
    package_price = models.FloatField()
    package_duration = models.IntegerField()
    package_description = models.CharField(max_length=100, default="")


class user_package_details(models.Model):
    login_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    premium_package_id = models.ForeignKey(premium_package, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=30)
    package_purchase_date = models.DateField(auto_now_add=True, editable=True)


class user_card_details(models.Model):
    login_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    card_no = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry_month = models.CharField(max_length=30)
    expiry_year = models.CharField(max_length=4)


class enquiry(models.Model):
    login_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default="")
    lastname = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=30, default="")
    enquiry_message = models.TextField()
    enquiry_subject = models.CharField(max_length=50)

