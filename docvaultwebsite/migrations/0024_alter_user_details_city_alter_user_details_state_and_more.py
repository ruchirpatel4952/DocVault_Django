# Generated by Django 4.0.2 on 2022-02-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docvaultwebsite', '0023_alter_user_details_city_alter_user_details_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='state',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='city',
        ),
        migrations.DeleteModel(
            name='state',
        ),
    ]
