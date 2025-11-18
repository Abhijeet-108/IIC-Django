from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.homepage , name = "admin-site"),
    path('post-create/' , views.postCreate , name = "post-create"),
    path('post-update/<int:pk>' , views.postEdit , name = "post-update"),
    path('post-delete/<int:pk>' , views.postDeletion , name = "post-delete"),

    path('achievment-create/' , views.achievCreate , name = "achievment-create"),
    path('achievment-update/<int:pk>' , views.achievEdit , name = "achievment-update"),
    path('achievment-delete/<int:pk>' , views.achievDeletion , name = "achievment-delete"),

    path('contactOrg-create/' , views.contactOrgCreate , name = "contactOrg-create"),
    path('contactOrg-update/<int:pk>' , views.contactOrgEdit , name = "contactOrg-update"),
    path('contactOrg-delete/<int:pk>' , views.contactOrgDeletion , name = "contactOrg-delete"),

    path('organisation-create/' , views.organisationCreate , name = "organisation-create"),
    path('organisation-update/<int:pk>' , views.organisationEdit , name = "organisation-update"),
    path('organisation-delete/<int:pk>' , views.organisationDeletion , name = "organisation-delete"),

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
