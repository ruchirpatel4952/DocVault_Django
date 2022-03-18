from django.contrib import admin

# Register your models here.

from .models import security_technique
from .models import document_details
from .models import document_privilege
from .models import feedback
from .models import premium_package
from .models import user_package_details
from .models import user_card_details
from .models import enquiry


class show_security_technique(admin.ModelAdmin):
    list_display = ['security_name']


class show_document_details(admin.ModelAdmin):
    list_display = (
        'login_id', 'document_security_technique', 'document_title', 'document_description',
        'document_status', 'document_type', 'document_password',
        'document_size', 'document_publish_date_time')


class show_document_privilege(admin.ModelAdmin):
    list_display = ('login_id', 'document_id', 'privilege_status')


class show_feedback(admin.ModelAdmin):
    list_display = ('login_id', 'firstname', 'lastname', 'email', 'feedback_comment')


class show_premium_package(admin.ModelAdmin):
    list_display = ('package_type', 'package_publish_date_time', 'package_status', 'package_price')


class show_user_package_details(admin.ModelAdmin):
    list_display = ('login_id', 'premium_package_id', 'payment_status', 'package_purchase_date')


class show_user_card_details(admin.ModelAdmin):
    list_display = ('login_id', 'card_no', 'cvv', 'expiry_month', 'expiry_year')


class show_enquiry(admin.ModelAdmin):
    list_display = ('login_id', 'firstname', 'lastname', 'email', 'enquiry_subject', 'enquiry_message')


admin.site.register(security_technique, show_security_technique)
admin.site.register(document_details, show_document_details)
admin.site.register(document_privilege, show_document_privilege)
admin.site.register(feedback, show_feedback)
admin.site.register(premium_package, show_premium_package)
admin.site.register(user_package_details, show_user_package_details)
admin.site.register(user_card_details, show_user_card_details)
admin.site.register(enquiry, show_enquiry)
