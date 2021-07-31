class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('sessionkey')
        if 'sessionkey' not in request.session:
            cart = self.session['sessionkey'] = {}
        self.cart = cart
    
    def add(self, book):
        book_id = book.id
        if book_id not in self.cart:
            self.cart[book_id] = {'price': str(book.price)}

        self.session.modified = True