from django.contrib import admin
from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'isbn', 'pages', 'cover', 'language']
