# Generated by Django 4.0.1 on 2022-02-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docvaultwebsite', '0005_enquiry_email_enquiry_firstname_enquiry_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='dob',
            field=models.DateField(default='0000-00-00'),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='dp',
            field=models.ImageField(default='dp_folder/user_dp.png', upload_to='dp_folder'),
        ),
    ]
