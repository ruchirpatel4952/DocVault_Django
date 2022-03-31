import hashlib
import random
from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect
from docvaultuser.models import premium_package, user_package_details
from .models import user_details
from .models import contact_us


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def aboutservices(request):
    return render(request, 'about.html#services')


def contact(request):
    return render(request, 'contact.html')


def premium(request):
    user = premium_package.objects.all().exclude(id=3)
    user2 = premium_package.objects.filter(id=3)
    return render(request, 'premium.html', {'context': user, 'context2': user2})


def ResetPasswordOTP(request):
    return render(request, 'ResetPasswordOTP.html')


def ResetPassword(request):
    return render(request, 'ResetPassword.html')


def setPassword(request):
    return render(request, 'signlog.html')


def signlog(request):
    return render(request, 'signlog.html')


# FOR REGISTRATION VALIDATION

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email').lower().strip()
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm-password')
        gender = request.POST.get('gender')
        phoneno = request.POST.get('phone_no')

        if password != confirmpassword:
            messages.info(request, 'Password does not match.')
            return render(request, 'signlog.html')

        try:
            user = user_details.objects.get(email=email)
            if user:
                messages.info(request, 'Account already exists. Please try other email.')
                return render(request, 'signlog.html')

        except user_details.DoesNotExist:
            passwordh = hashlib.md5(password.encode('utf-8')).hexdigest()

            query = user_details(firstname=firstname, lastname=lastname, email=email, password=passwordh,
                                 gender=gender, phone_no=phoneno, dp='dp_folder/defaultuser.jpg' ,
                                 confirm_password=passwordh,role=2, status=1,
                                 )
            query.save()

            query2 = user_package_details(login_id=user_details(id=query.id), premium_package_id=premium_package(id=3),
                                          payment_status=0)
            query2.save()

            return render(request, 'signlog.html')
    else:
        print("error")
    return render(request, 'signlog.html')


# FOR SIGNIN VALIDATION

def signin(request):
    if request.method == 'POST':
        useremail = request.POST.get('email').lower().strip()
        userpassword = request.POST.get('password').strip()

        try:
            userpasswordh = hashlib.md5(userpassword.encode('utf-8')).hexdigest()

            user = user_details.objects.get(email=useremail, password=userpasswordh)
            request.session['log_user_id'] = user.id
            request.session['log_user_email'] = user.email
            request.session['log_user_firstname'] = user.firstname
            request.session['log_user_lastname'] = user.lastname
            request.session.save()
        except user_details.DoesNotExist:
            user = None

        if user is not None:
            return redirect('/DocVaultIndex')
        else:
            messages.info(request, 'Invalid email or password')
            return render(request, 'signlog.html')
    else:
        print('error')
    return render(request, 'signlog.html')


# FOR LOGOUT ACCOUNT
def logout(request):
    try:
        del request.session['log_user_id']
        del request.session['log_user_email']
        del request.session['log_user_firstname']
        del request.session['log_user_lastname']
    except:
        pass
    return render(request, 'index.html')


# FOR CONTACTUS OF PREMIUM PAGE

def contactuspremium(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        query = contact_us(name=name, email=email, subject=subject, message=message)
        query.save()
        return render(request, 'signlog.html')
    else:
        print("error")
    return render(request, 'signlog.html')


def resetemail(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            query = user_details.objects.get(email=email)
            generatedpassword = random.randint(00000000, 99999999)

            passwordh = hashlib.md5(str(generatedpassword).encode('utf-8')).hexdigest()
            query.password = passwordh
            query.confirm_password = passwordh
            query.save()

            import smtplib

            gmail_user = 'docvault77@gmail.com'
            gmail_password = 'Docvault@9510714099'

            sent_from = gmail_user
            to = [email]
            subject = 'DocVault Account New Password.'
            body = 'Seems like you forgot your password for DocVault.\n ' \
                   'Your new password for your DocVault Account is ' \
                   ' ' + str(generatedpassword)

            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                print("Email sent successfully!")
            except Exception as ex:
                print("Something went wrong….", ex)
            message = 'New Password has been sent to your email.'
            return render(request, 'signlog.html', {'msg': message})
        except:
            messages.info(request, 'Account does not exist on that email.')
            return render(request, 'ResetPasswordOTP.html')
    else:
        print('error')
        return render(request, 'ResetPasswordOTP.html')


# FOR CONTACTUS OF CONTACT PAGE

def contactuscontact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        query = contact_us(name=name, email=email, subject=subject, message=message)
        query.save()
        return render(request, 'contact.html')
    else:
        print("error")
    return render(request, 'contact.html')
