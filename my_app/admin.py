from django.contrib import admin
from .models import Author, Books

admin.site.register(Books)
admin.site.register(Author)
# Register your models here.
