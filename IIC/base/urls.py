from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name = "home"),
    path('login/',views.loginFac , name = "login"),
    path('logout/',views.logoutFac , name = "logout"),

    path('query-create/' , views.queryCreate , name = "query-create"),
    path('query-delete/<int:pk>' , views.queryDeletion , name = "query-delete"),

]
