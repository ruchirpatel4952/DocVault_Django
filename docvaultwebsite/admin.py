from django.contrib import admin
from .models import user_details
from .models import contact_us


class show_user_details(admin.ModelAdmin):
    list_display = (
        'email', 'password', 'firstname', 'lastname', 'dob', 'phone_no', 'address', 'city', 'state')


class show_contact_us(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(user_details, show_user_details)
admin.site.register(contact_us, show_contact_us)
