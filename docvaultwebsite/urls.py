from os import path

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'$', views.index, name="index.html"),
    re_path('about', views.about, name="about.html"),
    re_path('aboutservices', views.aboutservices, name="about.html#services"),
    re_path('contactus', views.contact, name="contact.html"),
    re_path('premiumpackage', views.premium, name="premium.html"),
    re_path('ResetPasswordOTP', views.ResetPasswordOTP, name="ResetPasswordOTP.html"),
    # re_path('ResetPassword', views.ResetPassword, name="ResetPassword.html"),
    re_path('setPassword', views.setPassword, name="setPassword.html"),
    re_path('signlog', views.signlog, name="signlog.html"),
    re_path('signup', views.signup, name="signup"),
    re_path('signin', views.signin, name="signin"),
    re_path('contacts', views.contactuscontact, name="seecontact"),
    re_path('getstarted', views.contactuspremium, name="premiumcontact"),
    re_path('logout', views.logout, name='logout'),
    re_path('resetemail', views.resetemail, name='resetemail'),
]