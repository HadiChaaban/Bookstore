from django.shortcuts import render

from .models import Book

def all_products(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})