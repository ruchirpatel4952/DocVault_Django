# Generated by Django 4.0.1 on 2022-02-15 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docvaultwebsite', '0019_alter_user_details_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='login_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.user_details'),
        ),
    ]
