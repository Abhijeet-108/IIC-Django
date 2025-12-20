from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home , name = "home"),
    path('login/',views.loginFac , name = "login"),
    path('logout/',views.logoutFac , name = "logout"),

    path('signup/',views.registerFac , name = 'signup'),

    path('query-create/' , views.queryCreate , name = "query-create"),
    path('query-delete/<int:pk>' , views.queryDeletion , name = "query-delete"),
    
    path('activities/', views.activities , name = "activities"),
    path('contact/', views.contact , name = "contact"),
    path('gallery/', views.galleryPage , name = "gallery"),
    path('noticeboard/', views.noticeBoard , name = "notice"),
    path('achievments/', views.achiev , name = "achievments"),
    path('meetings/', views.meet , name = "meet"),
    
    path('team-members/', views.teamMenbers , name = "team_members"),
    path('add_teammember/', views.addteamMembers , name = "add_teammember"),
    path('update_teammember/<int:pk>/', views.updateteamMembers , name = "update_teammember"),
    path('delete_teammember/<int:pk>/', views.deleteteamMembers , name = "delete_teammember"),
    
    path('certificate/', views.certificates , name = "certificate"),
    path('add_certificate/', views.addcertificate , name = "add_certificate"),
    path('update_certificate/<int:pk>/', views.updatecertificate , name = "update_certificate"),
    path('delete_certificate/<int:pk>/', views.deletecertificate , name = "delete_certificate"),
    
    path('ipr/', views.iprs , name = "ipr"),
    path('add_ipr/', views.addipr , name = "add_ipr"),  
    path('update_ipr/<int:pk>/', views.updateipr , name = "update_ipr"),
    path('delete_ipr/<int:pk>/', views.deleteipr , name = "delete_ipr"),
    
    path('incubation/', views.incubations , name = "incubation"),
    path('add_incubation/', views.addincubation , name = "add_incubation"),  
    path('update_incubation/<int:pk>/', views.updateincubation , name = "update_incubation"),
    path('delete_incubation/<int:pk>/', views.deleteincubation , name = "delete_incubation"),
    

    path('activity-create/' , views.addactivity , name = "activity-create"),
    path('activity-update/<int:pk>' , views.updateactivity , name = "activity-update"),
    path('activity-delete/<int:pk>' , views.deleteactivity , name = "activity-delete"),


    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("reset-password/", views.reset_password, name="reset_password"),


] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
