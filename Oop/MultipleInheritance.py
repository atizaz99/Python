class Phone:
    def __init__(self, price, brand, camera):
        print('inside phone constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print('Buying a phone')
    
class Product:
    def review(self):
        print('Customer Review')

'''
Multiple inheritance
MRO: Method resolution order: 
it mean always that the object will always call the method of first class define in multiple inheritance.
'''
    
class SmartPhone(Phone, Product):
    pass 
smart_phone = SmartPhone(50000, 'Samsung', '20MP')
smart_phone.buy()
smart_phone.review()