from django.contrib import admin
from .models import *


class BookModal(admin.StackedInline):
    model = Book


@admin.register(Publisher)
class PublishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'addr')
    fields = ('name', 'addr')
    search_fields = ['name', 'addr']
    inlines = [BookModal]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ISBN', 'author', 'publisher', 'publish_date', 'catagoery', 'picture')
    fields = ('name', 'ISBN', 'author', 'publisher', 'publish_date', 'catagoery', 'picture')
    list_filter = ['publisher']
    search_fields = ['name', 'ISBN', 'author', 'publisher', 'publish_date', 'catagoery']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'tel')
    fields = ('name', 'age', 'tel')
    search_fields = ['name', 'age', 'tel']
    filter_horizontal = ('book',)
    list_filter = ['book']