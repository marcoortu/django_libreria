from django.contrib import admin

from libreria.models import *

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Order , OrderAdmin)
