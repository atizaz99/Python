class Product:
    def review(self):
        print('Product Customer Review')

class Phone(Product):
    def __init__(self, price, brand, camera):
        print('Inside Phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class SmartPhone(Phone):
    pass
s = SmartPhone(200, 'phone', 23)
p = Phone(100, 'Samsung', 32)
s.buy()
s.review()
p.review()
