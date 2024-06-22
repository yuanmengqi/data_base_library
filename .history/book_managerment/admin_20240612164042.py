from django.contrib import admin
from .models import *


class BookModal(admin.StackedInline):
    model = Book


@admin.register(Publisher_info)
class PublishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'addr')
    fields = ('name', 'addr')
    search_fields = ['name', 'addr']
    inlines = [BookModal]

    def books(self, obj):
        return [book.title for book in obj.book_set.all()]


@admin.register(Book_info)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ISBN', 'author', 'publisher', 'publish_date', 'catagoery', 'picture')
    fields = ('title', 'ISBN', 'authors', 'publisher', 'publish_date', 'catagoery', 'picture')
    list_filter = ['publisher']
    search_fields = ['title', 'ISBN', 'authors', 'publisher', 'publish_date', 'catagoery']


    def author(self, obj):
        return [author.name for author in obj.authors.all()]

    def publish_name(self, obj):
        return obj.publish.name

    filter_horizontal = ('author',)


@admin.register(Author_info)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'tel')
    fields = ('name', 'age', 'tel')
    search_fields = ['name', 'age', 'tel']
    filter_horizontal = ('book',)
    list_filter = ['book']

    def books(self, obj):
        return [book.title for book in obj.book_set.all()]
