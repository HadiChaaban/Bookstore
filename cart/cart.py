from decimal import Decimal

from store.models import Book

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('sessionkey')
        if 'sessionkey' not in request.session:
            cart = self.session['sessionkey'] = {}
        self.cart = cart
    
    def add(self, book, qty):
        book_id = book.id
        if book_id not in self.cart:
            self.cart[book_id] = {'price': str(book.price), 'qty':int(qty)}

        self.session.modified = True

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        cart = self.cart.copy()

        for book in books:
            cart[str(book.id)]['book'] = book

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
        
    def __len__(self):
        return sum(book['qty'] for book in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    
    def delete(self, book):
        book_id = str(book)

        if book_id in self.cart:
            del self.cart[book_id]
            print(book_id)
            self.save()

    def update(self, book, qty):
        book_id = str(book)
        if book_id in self.cart:
            self.cart[book_id]['qty'] = qty
        self.save()

    def save(self):
        self.session.modified = True