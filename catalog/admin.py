from django.contrib import admin
from .models import Book, Author, Genre, Language, BookInstance
from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Language)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('genre',)
    search_fields = ('title', 'author__first_name', 'author__last_name')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status_color', 'img_image')
    list_filter = ('status', 'due_back')