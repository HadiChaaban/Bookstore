from django.contrib import admin
from .models import Book

@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'user_rating', 'price', 'year', 'genre', 'slug']
    prepopulated_fields = {'slug': ('title',)}
