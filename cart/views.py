from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse


from .cart import Cart
from store.models import Book
# Create your views here.

def cart_summary(request):
    return render(request, 'store/cart/cart.html')

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book = get_object_or_404(Book, id=book_id)
        cart.add(book=book)
        response = JsonResponse({'test':'data'})
        return response