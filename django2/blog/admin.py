from django.contrib import admin

# Register your models here.
from .models import Blog, Author, Book, Publisher, BlogAdmin

admin.site.register(Blog, BlogAdmin)


class AutAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


class PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')

admin.site.register(Author, AutAdmin)
admin.site.register(Publisher, PubAdmin)
admin.site.register(Book,BookAdmin)
