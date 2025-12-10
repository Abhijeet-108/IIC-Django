from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.homepage , name = "admin-site"),
    path('profile/', views.profilePage , name = "admin-profile"),

    path('info-update' , views.iicInfoEdit , name = "info-update"),

    path('post-create/' , views.postCreate , name = "post-create"),
    path('post-update/<int:pk>' , views.postEdit , name = "post-update"),
    path('post-delete/<int:pk>' , views.postDeletion , name = "post-delete"),

    path('meet-create/' , views.add_meetform , name = "meet-create"),
    path('meet-update/<int:pk>' , views.update_meetform , name = "meet-update"),
    path('meet-delete/<int:pk>' , views.delete_meetform , name = "meet-delete"),

    path('gallery-create/' , views.galleryCreate , name = "gallery-create"),
    path('gallery-delete/<int:pk>' , views.galleryDeletion , name = "gallery-delete"),

    path('notice-create/' , views.noticeCreate , name = "notice-create"),
    path('notice-update/<int:pk>' , views.noticeEdit , name = "notice-update"),
    path('notice-delete/<int:pk>' , views.noticeDeletion , name = "notice-delete"),


    path('achievment-create/' , views.achievCreate , name = "achievment-create"),
    path('achievment-approve/<int:pk>' , views.approveAchi , name = "achievment-approve"),
    path('achievment-update/<int:pk>' , views.achievEdit , name = "achievment-update"),
    path('achievment-delete/<int:pk>' , views.achievDeletion , name = "achievment-delete"),

    path('contactOrg-create/' , views.contactOrgCreate , name = "contactOrg-create"),
    path('contactOrg-update/<int:pk>' , views.contactOrgEdit , name = "contactOrg-update"),
    path('contactOrg-delete/<int:pk>' , views.contactOrgDeletion , name = "contactOrg-delete"),

    path('organisation-create/' , views.organisationCreate , name = "organisation-create"),
    path('organisation-update/<int:pk>' , views.organisationEdit , name = "organisation-update"),
    path('organisation-delete/<int:pk>' , views.organisationDeletion , name = "organisation-delete"),

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
