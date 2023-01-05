from django.contrib import admin

from library_m_s.models import books, staf_user,student

# Register your models here.
admin.site.register(staf_user)
admin.site.register(books)
admin.site.register(student)