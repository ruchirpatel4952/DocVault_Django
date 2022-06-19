from django.contrib import admin
from .models import user_details
from .models import contact_us


class show_user_details(admin.ModelAdmin):
    list_display = (
        'email', 'firstname','password', 'lastname', 'gender', 'dob', 'phone_no', 'city', 'state', 'address')


class show_contact_us(admin.ModelAdmin):
    list_display = ('email', 'name', 'subject', 'message')


admin.site.register(user_details, show_user_details)
admin.site.register(contact_us, show_contact_us)
