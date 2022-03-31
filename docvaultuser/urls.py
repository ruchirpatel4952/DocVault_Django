from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path('DocVaultIndex', views.DocVaultIndex, name="DocVaultIndex.html"),
    re_path('DocVaultMyUploads', views.DocVaultMyUploads, name="DocVaultMyUploads.html"),
    re_path('DocVaultDownloadFiles', views.showpublic, name="DocVaultDownloadFiles.html"),
    re_path('DocVaultEnquiry', views.DocVaultEnquiry, name="DocVaultEnquiry.html"),
    re_path('DocVaultFeedback', views.DocVaultFeedback, name="DocVaultFeedback.html"),

    path('DocVaultFileUploadPasswordCheck/<int:id>', views.DocVaultFileUploadPasswordCheck,
            name="DocVaultFileUploadPasswordCheck.html"),

    re_path('DocVaultFileUploadPrivate', views.DocVaultFileUploadPrivate, name="DocVaultFileUploadPrivate.html"),
    re_path('DocVaultFileUploadPublic', views.DocVaultFileUploadPublic, name="DocVaultFileUploadPublic.html"),
    re_path('DocVaultFileUploadUserPrivilege', views.DocVaultFileUploadUserPrivilege,
            name="DocVaultFileUploadUserPrivilege.html"),

    path('DocVaultPayment/<int:id>', views.DocVaultPayment, name="DocVaultPayment.html"),
    re_path('DocVaultPremium', views.DocVaultPremium, name="DocVaultPremium.html"),

    re_path('DocVaultProfile', views.DocVaultProfile, name="DocVaultProfile.html"),
    re_path('DocVaultSetPassword', views.DocVaultSetPassword, name="DocVaultSetPassword.html"),
    re_path('DocVaultSharedFiles', views.DocVaultSharedFiles, name="DocVaultSharedFiles.html"),

    path('DocVaultShareEmail/<int:id>', views.DocVaultShareEmail, name="DocVaultShareEmail.html"),
    re_path('DocVaultShareFiles', views.DocVaultShareFiles, name="DocVaultShareFiles.html"),
    re_path('DocVaultDocumentCheck', views.DocVaultDocumentCheck, name="DocVaultDocumentCheck.html"),
    re_path('DocVaultRecycle', views.DocVaultRecycle, name="DocVaultRecycle.html"),


    re_path('Feedback', views.Feedback, name="Feedback"),
    re_path('Enquiry', views.Enquiry, name="Enquiry"),
    re_path('PaymentDetails', views.PaymentDetails, name="PaymentDetails"),
    re_path('Profile', views.Profile, name="Profile"),
    re_path('uploadPublic', views.uploadPublic, name="uploadPublic"),
    re_path('uploadPrivate', views.uploadPrivate, name="uploadPrivate"),
    re_path('uploadUserPrivilege', views.uploadUserPrivilege, name="uploadUserPrivilege"),
    re_path('showpublic', views.showpublic, name="showpublic"),
    re_path('showprivate', views.showprivate, name="showprivate"),
    re_path('showup', views.showup, name="showup"),
    re_path('DocVaultSet', views.DocVaultSet, name="DocVaultSet"),


    path('delete/<int:id>', views.delete, name="delete"),
    path('restore/<int:id>', views.restore, name="restore"),
    path('movetobin/<int:id>', views.movetobin, name="movetobin"),
    path('share/<int:id>', views.share, name="share"),
    path('unsend', views.unsend, name="unsend"),
    path('unsendselect/<int:id>', views.DocVaultUnsendSelect,name="unsend_select"),
    re_path('insertPrivilege', views.insertPrivilege, name='insertPrivilege'),
    re_path('checkPassword', views.checkPassword, name='checkPassword'),

]
