# Generated by Django 4.0.2 on 2022-03-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docvaultuser', '0005_premium_package_package_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premium_package',
            name='package_duration',
            field=models.IntegerField(),
        ),
    ]
