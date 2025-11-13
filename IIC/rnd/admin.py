from django.contrib import admin
from .models import dept , facult , suff , patent , book , bookChapter , conference , journal , copyright , basicDetails
# Register your models here.

admin.site.register(dept)
admin.site.register(facult)
admin.site.register(suff)
admin.site.register(patent)
admin.site.register(book)
admin.site.register(bookChapter)
admin.site.register(conference)
admin.site.register(journal)
admin.site.register(copyright)
admin.site.register(basicDetails)