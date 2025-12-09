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

    path('activity-create/' , views.addactivity , name = "activity-create"),
    path('activity-update/<int:pk>' , views.updateactivity , name = "activity-update"),
    path('activity-delete/<int:pk>' , views.deleteactivity , name = "activity-delete"),


] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
