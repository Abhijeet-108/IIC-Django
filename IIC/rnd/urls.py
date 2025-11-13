from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.rnd , name = "research"),
    path('department/<int:pk>', views.depart , name = "depart"),
    path('faculty/<int:pk>', views.facul , name = "facul"),
    # ----------- patent -------------------
    path('patentform/', views.add_form, name="form"),
    path('patentform-update/<int:pk>', views.update_form, name="updateform"),
    path('patentform-delete/<int:pk>', views.delete_form, name="deletePatentform"),
    # ------------- dept ------------------------
    path('deptform/', views.add_deptform, name="deptform"),
    path('deptform-update/<int:pk>', views.update_deptform, name="deptform"),
    path('deptform-delete/<int:pk>', views.delete_deptform, name="deptform"),
    
    # ------------- Book -------------------
    path('bookform/', views.add_bookform, name="bookform"),
    path('bookform-update/<int:pk>', views.update_bookform, name="updatebookform"),
    path('bookform-delete/<int:pk>', views.delete_bookform, name="deletebookform"),

    path('basic-create/' , views.basicCreate , name = "basic-create"),
    path('basic-update/<int:pk>' , views.basicEdit , name = "basic-update"),
    path('basic-delete/<int:pk>' , views.basicDeletion , name = "basic-delete"),

]
    # ------------- Book Chapter -------------------
    path('bookChapterform/', views.add_bookChapterform, name="bookChapterform"),
    path('bookChapterform-update/<int:pk>', views.update_bookChapterform, name="updatebookChapterform"),
    path('bookChapterform-delete/<int:pk>', views.delete_bookChapterform, name="deletebookChapterform"),

    # ------------- Faculty -------------------
    path('facultform/', views.add_facultform, name="facultform"),
    path('facultform-update/<int:pk>', views.update_facultform, name="updatefacultform"),
    path('facultform-delete/<int:pk>', views.delete_facultform, name="deletefacultform"),

    # ------------- Suff -------------------
    path('suffform/', views.add_suffform, name="suffform"),
    path('suffform-update/<int:pk>', views.update_suffform, name="updatesuffform"),
    path('suffform-delete/<int:pk>', views.delete_suffform, name="deletesuffform"),

    # ------------- Copyright -------------------
    path('copyrightform/', views.add_copyrightform, name="copyrightform"),
    path('copyrightform-update/<int:pk>', views.update_copyrightform, name="updatecopyrightform"),
    path('copyrightform-delete/<int:pk>', views.delete_copyrightform, name="deletecopyrightform"),

    # ------------- Conference -------------------
    path('conferenceform/', views.add_conferenceform, name="conferenceform"),
    path('conferenceform-update/<int:pk>', views.update_conferenceform, name="updateconferenceform"),
    path('conferenceform-delete/<int:pk>', views.delete_conferenceform, name="deleteconferenceform"),

    # ------------- Journal -------------------
    path('journalform/', views.add_journalform, name="journalform"),
    path('journalform-update/<int:pk>', views.update_journalform, name="updatejournalform"),
    path('journalform-delete/<int:pk>', views.delete_journalform, name="deletejournalform"),
    
]
