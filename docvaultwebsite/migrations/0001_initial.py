# Generated by Django 4.0.1 on 2022-02-06 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='document_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='document_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_title', models.CharField(max_length=30)),
                ('document_description', models.TextField(default='')),
                ('document_status', models.CharField(max_length=30)),
                ('document_size', models.FloatField()),
                ('document_path', models.CharField(max_length=150)),
                ('document_publish_date_time', models.DateTimeField(auto_now_add=True)),
                ('document_password', models.CharField(max_length=30)),
                ('document_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.document_category')),
            ],
        ),
        migrations.CreateModel(
            name='premium_package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(max_length=30)),
                ('package_publish_date_time', models.DateTimeField(auto_now_add=True)),
                ('package_status', models.CharField(max_length=30)),
                ('package_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='security_technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
                ('firstname', models.CharField(default='', max_length=30)),
                ('lastname', models.CharField(default='', max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('phone_no', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('dp', models.ImageField(upload_to='dp_folder')),
                ('role', models.IntegerField()),
                ('status', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.state')),
            ],
        ),
        migrations.CreateModel(
            name='user_package_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=30)),
                ('package_purchase_date', models.DateTimeField()),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.user_details')),
                ('premium_package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.premium_package')),
            ],
        ),
        migrations.CreateModel(
            name='user_card_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('expiry_month', models.CharField(max_length=2)),
                ('expiry_year', models.CharField(max_length=4)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.user_details')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_comment', models.TextField()),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.user_details')),
            ],
        ),
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_message', models.TextField()),
                ('enquiry_subject', models.CharField(max_length=50)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.user_details')),
            ],
        ),
        migrations.CreateModel(
            name='document_privilege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privilege_status', models.IntegerField()),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.document_details')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.user_details')),
            ],
        ),
        migrations.AddField(
            model_name='document_details',
            name='document_security_technique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.security_technique'),
        ),
        migrations.AddField(
            model_name='document_details',
            name='login_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.user_details'),
        ),
        migrations.AddField(
            model_name='city',
            name='stateid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docvaultwebsite.state'),
        ),
    ]
