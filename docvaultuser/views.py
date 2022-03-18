import hashlib
import os
from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
import docvaultwebsite
from docvaultwebsite.models import user_details
from .models import user_card_details, enquiry, feedback, document_details, security_technique, document_privilege, \
    user_package_details, premium_package


def DocVaultIndex(request):
    try:
        if request.session.is_empty():
            return render(request, 'signlog.html')

        else:
            try:

                uid = request.session['log_user_id']
                user = user_details.objects.get(id=uid)

                myuploadcount = document_details.objects.all().filter(login_id=request.session['log_user_id'])
                sharedwithmecount = document_privilege.objects.all().filter(login_id=request.session['log_user_id'])
                mypubliccount = document_details.objects.all().filter(login_id=request.session['log_user_id'],
                                                                      document_security_technique='1')
                myprivatecount = document_details.objects.all().filter(login_id=request.session['log_user_id'],
                                                                       document_security_technique='2')
                myuserprivilege = document_details.objects.all().filter(login_id=request.session['log_user_id'],
                                                                        document_security_technique='3')

                package = user_package_details.objects.get(login_id=user_details(uid))
                packagestr = str(package.premium_package_id)

                packagedetails = premium_package.objects.get(id=packagestr[-2])

                context = {
                    'myuploadscount': len(myuploadcount),
                    'sharedwithmecount': len(sharedwithmecount),
                    'publicdocuments': len(mypubliccount),
                    'privatedocuments': len(myprivatecount),
                    'userprivilegedocuments': len(myuserprivilege),
                    'packagename': packagedetails.package_type

                }

            except user_details.DoesNotExist:
                user = None
            return render(request, 'DocVaultIndex.html', context)
    except:
        print("Error")
    return render(request, 'signlog.html')


def DocVaultMyUploads(request):
    getdata = document_details.objects.all().filter(login_id=request.session['log_user_id']).filter(document_bin=0)
    return render(request, 'DocVaultMyUploads.html', {'context': getdata})


def DocVaultRecycle(request):
    getdata = document_details.objects.all().filter(login_id=request.session['log_user_id']).filter(document_bin=1)
    return render(request, 'DocVaultRecycle.html', {'context': getdata})


def DocVaultDocumentCheck(request):
    return render(request, "DocVaultDocumentCheck.html")


def DocVaultDownloadFiles(request):
    return render(request, "DocVaultDownloadFiles.html")


def DocVaultEnquiry(request):
    user = user_details.objects.get(id=request.session['log_user_id'])
    context = {
        'firstname': user.firstname,
        'lastname': user.lastname,
        'email': user.email,
    }
    return render(request, 'DocVaultEnquiry.html', context)


def DocVaultFeedback(request):
    user = user_details.objects.get(id=request.session['log_user_id'])
    context = {
        'firstname': user.firstname,
        'lastname': user.lastname,
        'email': user.email,
    }
    return render(request, 'DocVaultFeedback.html', context)


def DocVaultFileUploadPasswordCheck(request, id):
    return render(request, 'DocVaultFileUploadPasswordCheck.html',
                  {'docid': id, 'dp': request.session['log_user_dp']})


def checkPassword(request):
    if request.method == "POST":
        password = request.POST.get('password')
        docid = request.POST.get('docid')
        mypath = '/DocVaultFileUploadPasswordCheck/' + str(docid)
        query = document_details.objects.get(id=docid)
        try:
            passwordh = hashlib.md5(password.encode('utf-8')).hexdigest()
            if passwordh == query.document_password:
                return render(request, 'DocVaultFileUploadPasswordCheck.html', {'doclink': query.document})
            else:
                messages.info(request, 'Wrong Password')
                return redirect(mypath)
        except:
            messages.info(request, 'Wrong Password')
            return redirect(mypath)
    else:
        print("error")


def DocVaultFileUploadPrivate(request):
    return render(request, 'DocVaultFileUploadPrivate.html')


def DocVaultFileUploadPublic(request):
    return render(request, 'DocVaultFileUploadPublic.html')


def DocVaultFileUploadUserPrivilege(request):
    return render(request, 'DocVaultFileUploadUserPrivilege.html')


def DocVaultPayment(request, id):
    return render(request, 'DocVaultPayment.html', {'packageid': id})


def DocVaultPremium(request):
    pack = premium_package.objects.all().exclude(id=3).order_by('package_price')
    basic = premium_package.objects.get(id=3)
    return render(request, 'DocVaultPremium.html', {'context':pack,'basic': basic})


def DocVaultProfile(request):
    user = user_details.objects.get(id=request.session['log_user_id'])
    context = {
        'firstname': user.firstname,
        'lastname': user.lastname,
        'email': user.email,
        'password': user.password,
        'confirmpassword': user.confirm_password,
        'gender': user.gender,
        'dob': str(user.dob),
        'address': user.address,
        'phoneno': user.phone_no,
        'city': user.city,
        'state': user.state,
        'dp': user.dp
    }
    return render(request, 'DocVaultProfile.html', context)


def DocVaultSharedFiles(request):
    getdata = document_privilege.objects.all().filter(login_id=request.session['log_user_id'])
    return render(request, 'DocVaultSharedFiles.html', {'context': getdata})


def DocVaultShareEmail(request, id):
    return render(request, 'DocVaultShareEmail.html', {'docid': id})


def DocVaultShareFiles(request):
    getdata = document_details.objects.all()
    return render(request, "DocVaultShareFiles.html", {'context': getdata})


def Feedback(request):
    if request.method == 'POST':

        message = request.POST.get('message')

        user = user_details.objects.get(id=request.session['log_user_id'])
        query = feedback(login_id=user_details(request.session['log_user_id']), firstname=user.firstname,
                         lastname=user.lastname,
                         email=user.email,
                         feedback_comment=message)
        query.save()

        return redirect('/DocVaultIndex')
    else:
        print("error")
    return render(request, 'DocVaultFeedback.html')


def Enquiry(request):
    if request.method == 'POST':

        subject = request.POST.get('subject')
        message = request.POST.get('message')

        user = user_details.objects.get(id=request.session['log_user_id'])
        query = enquiry(login_id=user_details(request.session['log_user_id']), firstname=user.firstname,
                        lastname=user.lastname,
                        email=user.email, enquiry_subject=subject,
                        enquiry_message=message)
        query.save()
        return redirect('/DocVaultIndex')
    else:
        print("error")
    return render(request, 'DocVaultEnquiry.html')


def PaymentDetails(request):
    if request.method == 'POST':
        cardnumber = request.POST.get('cardnumber')
        expirymonth = request.POST.get('expirymonth')
        expiryyear = request.POST.get('expiryyear')
        cvv = request.POST.get('cvv')
        packageid = request.POST.get('packageid')

        cardnumber = cardnumber.replace(" ", "")
        cvv = cvv.replace(" ", "")

        if len(cardnumber) == 16 or len(cvv) == 3:
            if len(cardnumber) == 16:
                if len(cvv) == 3:
                    query = user_card_details(login_id=user_details(request.session['log_user_id']), card_no=cardnumber,
                                              expiry_month=expirymonth, expiry_year=expiryyear, cvv=cvv)
                    query.save()

                    query2 = user_package_details.objects.get(login_id=request.session['log_user_id'])
                    query2.premium_package_id = premium_package(packageid)
                    query2.payment_status = 1
                    query2.package_purchase_date = date.today()
                    query2.save()

                    query3 = premium_package.objects.get(id=packageid)

                    context = {
                        'package_name': query3.package_type,
                        'username': str(request.session['log_user_firstname']) + str(" ") + str(
                            request.session['log_user_lastname']),
                        'phone': request.session['log_user_phoneno'],
                        'address': request.session['log_user_address'],
                        'email': request.session['log_user_email'],
                        'city': request.session['log_user_city'],
                        'state': request.session['log_user_state'],
                        'amount': query3.package_price,
                        'duration': query3.package_duration,
                        'purchasetime': query2.package_purchase_date
                    }
                else:
                    messages.info(request, "CVV must be of 3 digits")
                    path = "/DocVaultPayment/" + str(packageid)
                    return redirect(path)
            else:
                messages.info(request, "Card Number must be of 16 digits")
                path = "/DocVaultPayment/" + str(packageid)
                return redirect(path)
        else:
            messages.info(request, "Card Number must be of 16 digits. CVV must be of 3 digits")
            path = "/DocVaultPayment/" + str(packageid)
            return redirect(path)
    else:
        print("error")
    return render(request, "DocVaultInvoice.html", context)


def uploadPublic(request):
    if request.method == 'POST':
        f_title = request.POST.get('file_title')
        f_desc = request.POST.get('file_desc')
        f_file = request.FILES['file']
        f_type = os.path.splitext(str(f_file))[1]
        f_status = "available"
        f_size = convert_bytes(request.FILES['file'].size)
        f_password = ""

        userdocs = document_details.objects.all().filter(login_id=request.session['log_user_id'])
        userpackage = user_package_details.objects.get(login_id=request.session['log_user_id'])
        userpackagestr = str(userpackage.premium_package_id)
        userpackageid = userpackagestr[-2]

        if (len(userdocs) + 1 < 3 and userpackageid == '3') or userpackageid == '1' or userpackageid == '2':
            query = document_details(login_id=user_details(id=request.session['log_user_id']), document_type=f_type,
                                     document_security_technique=security_technique(id=1), document_title=f_title,
                                     document_description=f_desc, document_status=f_status,
                                     document_size=f_size, document=f_file, document_password=f_password,
                                     document_bin=0)
            query.save()
            return redirect('/DocVaultMyUploads')
        else:
            return redirect('/DocVaultDocumentCheck')
    else:
        print('error')

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def uploadPrivate(request):
    if request.method == 'POST':
        f_title = request.POST.get('file_title')
        f_desc = request.POST.get('file_desc')
        f_file = request.FILES['file']
        f_type = os.path.splitext(str(f_file))[1]
        f_status = "available"
        f_size = convert_bytes(request.FILES['file'].size)
        f_password = request.POST.get('file_password')
        f_confirmpassword = request.POST.get('file_confirmpassword')

        if f_password != f_confirmpassword:
            messages.info(request, 'Password does not match.')
            return render(request, 'DocVaultFileUploadPrivate.html')

        userdocs = document_details.objects.all().filter(login_id=request.session['log_user_id'])
        userpackage = user_package_details.objects.get(login_id=request.session['log_user_id'])
        userpackagestr = str(userpackage.premium_package_id)
        userpackageid = userpackagestr[-2]

        if (len(userdocs) + 1 < 15 and userpackageid == '3') or userpackageid == '1' or userpackageid == '2':
            f_passwordh = hashlib.md5(f_password.encode('utf-8')).hexdigest()
            query = document_details(login_id=user_details(id=request.session['log_user_id']), document_type=f_type,
                                     document_security_technique=security_technique(id=2), document_title=f_title,
                                     document_description=f_desc, document_status=f_status,
                                     document_size=f_size, document=f_file, document_password=f_passwordh,
                                     document_bin=0)
            query.save()
            return redirect('/DocVaultMyUploads')
        else:
            return redirect('/DocVaultIndex')
    else:
        print('error')


def uploadUserPrivilege(request):
    if request.method == 'POST':
        f_title = request.POST.get('file_title')
        f_desc = request.POST.get('file_desc')
        f_file = request.FILES['file']
        f_type = os.path.splitext(str(f_file))[1]
        f_status = "available"
        f_size = convert_bytes(request.FILES['file'].size)
        f_password = ""

        userdocs = document_details.objects.all().filter(login_id=request.session['log_user_id'])
        userpackage = user_package_details.objects.get(login_id=request.session['log_user_id'])
        userpackagestr = str(userpackage.premium_package_id)
        userpackageid = userpackagestr[-2]

        if (len(userdocs) + 1 < 15 and userpackageid == '3') or userpackageid == '1' or userpackageid == '2':
            query = document_details(login_id=user_details(id=request.session['log_user_id']), document_type=f_type,
                                     document_security_technique=security_technique(id=3), document_title=f_title,
                                     document_description=f_desc, document_status=f_status,
                                     document_size=f_size, document=f_file, document_password=f_password,
                                     document_bin=0)
            query.save()
            return redirect('/DocVaultMyUploads')
        else:
            return redirect('/DocVaultIndex')
    else:
        print('error')


def showpublic(request):
    getdata = document_details.objects.all().filter(document_security_technique=1).exclude(
        login_id=user_details(id=request.session['log_user_id']))
    return render(request, 'DocVaultDownloadFiles.html', {'context': getdata})


def showprivate(request):
    getdata = document_details.objects.all().filter(document_security_technique=2).exclude(
        login_id=user_details(id=request.session['log_user_id']))
    return render(request, 'DocVaultShareFilesPrivate.html', {'context': getdata})


def showup(request):
    getdata = document_details.objects.all().filter(document_security_technique=3).filter(
        login_id=request.session['log_user_id']).exclude(document_bin=1).exclude(document_sent=1)

    getdata1 = document_details.objects.all().filter(document_security_technique=3).filter(
        login_id=request.session['log_user_id']).exclude(document_bin=1).filter(document_sent=1)
    return render(request, 'DocVaultShareFilesUP.html', {'context': getdata,'context1': getdata1})


def delete(request, id):
    query = document_details.objects.get(id=id)
    query.delete()
    return redirect('/DocVaultRecycle')


def restore(request, id):
    query = document_details.objects.get(id=id)
    query.document_bin = 0
    query.save()
    return redirect('/DocVaultRecycle')


def movetobin(request, id):
    query = document_details.objects.get(id=id)
    query.document_bin = 1
    query.save()
    return redirect('/DocVaultMyUploads')


def share(request, id):
    query = document_details.objects.get(id=id)
    return redirect('/DocVaultShareEmail')


def insertPrivilege(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower().strip()
        docid = request.POST.get('docid')
        mypath = '/DocVaultShareEmail/' + docid
        if request.session['log_user_email'] == email:
            messages.info(request, 'Cant send to owner.')
            return redirect(mypath)
        else:
            try:
                user = user_details.objects.get(email=email)
                login = user.id

                try:
                    query = document_privilege.objects.get(document_id=docid,sent_to=email)
                    messages.info(request, 'object already exists.')
                    return redirect(mypath)

                except:
                    query = document_privilege(login_id=user_details(id=login), document_id=document_details(id=docid),
                                               privilege_status=1, sent_to=email)
                    q1 = document_details.objects.get(id=docid)
                    q1.document_sent = 1
                    query.save()
                    q1.save()
                    return redirect('/showup')
            except:
                messages.info(request, 'Email does not exist.')
                return redirect(mypath)
    else:
        print('error')


def Profile(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        gender = request.POST.get('gender')
        phoneno = request.POST.get('phoneno')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        CITY = request.POST.get('city')
        STATE = request.POST.get('state')

        if password != confirmpassword:
            messages.info(request, 'Password does not match.')
            return redirect("/DocVaultProfile")
        else:
            try:
                pic = request.FILES['pic']
                request.session['log_user_dp'] = "dp_folder/" + str(pic)
            except:
                pic = request.session['log_user_dp']
                request.session['log_user_dp'] = str(pic)

            passwordh = hashlib.md5(password.encode('utf-8')).hexdigest()
            query = user_details.objects.get(id=request.session['log_user_id'])
            query.password = passwordh
            query.confirm_password = passwordh
            query.phone_no = phoneno
            query.dob = str(dob)
            query.address = str(address)
            query.dp = pic
            query.city = CITY
            query.state = STATE
            query.save()

            request.session['log_user_password'] = password
            request.session['log_user_confirmpassword'] = confirmpassword
            request.session['log_user_phoneno'] = phoneno
            request.session['log_user_dob'] = str(dob)
            request.session['log_user_address'] = str(address)
            request.session['log_user_city'] = str(CITY)
            request.session['log_user_state'] = str(STATE)
            request.session.save()

            return redirect("/DocVaultProfile")
    else:
        print('error')

def unsend(request):
    email = request.POST.get('email')
    docid = request.POST.get('docid')
    mypath = '/unsendselect/' + str(docid)

    try:
        p = document_privilege.objects.get(document_id = docid, sent_to = email)
        p.delete()
        try:
            p = document_privilege.objects.get(document_id = docid)
            return redirect('/showup')
        except:
            d = document_details.objects.get(id = docid)
            d.document_sent = 0
            d.save()
            return redirect('/showup')
    except:
        messages.info(request, 'Email does not exist.')
        return redirect(mypath)

def DocVaultUnsendSelect(request, id):
    p = document_privilege.objects.all().filter(document_id=id)
    return  render(request, 'DocVaultUnsendSelect.html', {'context':p, 'docid':id})