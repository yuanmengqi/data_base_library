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

    def books(self, obj):
        return [book.title for book in obj.book_set.all()]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ISBN', 'author', 'publisher', 'publish_date', 'catagoery', 'picture')
    fields = ('title', 'price', 'pub_date', "authors")
    search_fields = ['title', 'price', 'pub_date']

    def author(self, obj):
        return [author.name for author in obj.authors.all()]

    def publish_name(self, obj):
        return obj.publish.name

    filter_horizontal = ('authors',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'tel', 'addr', 'birthday', 'books')
    fields = ('name', 'age', 'gender', 'tel', 'addr', 'birthday')
    list_filter = ['gender']
    search_fields = ['name', 'age', 'gender', 'tel', 'addr', 'birthday']

    def books(self, obj):
        return [book.title for book in obj.book_set.all()]
