from . import ab2
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

def team(req):
    return ab2.jo(req)

urlpatterns = [
    path('team', team , name = "team"),
]