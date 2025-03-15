from django.contrib import admin
from .models import *

# Register your models here.
class AdminBook(admin.ModelAdmin):
    list_display = ['id','title','author','isbn','language']

class AdminLibrary(admin.ModelAdmin):
    list_display = ['id','book','user']


admin.site.register(Book, AdminBook)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Library, AdminLibrary)
