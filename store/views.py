from django.shortcuts import render, get_object_or_404

from .models import Book

def all_products(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})

def product_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'store/books/detail.html', {'book': book})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        books = Book.objects.filter(title__contains=search)
        return render(request, 'store/searchbar.html', {'books': books})