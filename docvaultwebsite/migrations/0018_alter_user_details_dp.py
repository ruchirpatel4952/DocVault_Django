# Generated by Django 4.0.1 on 2022-02-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docvaultwebsite', '0017_alter_user_details_confirm_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='dp',
            field=models.ImageField(default='dp_folder/defaultuser.jpg', upload_to='media/dp_folder'),
        ),
    ]
