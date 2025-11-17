from django.contrib import admin
from .models import posts , organisation , contactOrg , achievement ,querys, iicInfo , meeting , notice , gallery , activity

# Register your models here.

admin.site.register(posts)
admin.site.register(organisation)
admin.site.register(contactOrg)
admin.site.register(achievement)
admin.site.register(querys)
admin.site.register(iicInfo)
admin.site.register(meeting)
admin.site.register(notice)
admin.site.register(gallery)
admin.site.register(activity)