class Phone:
    def __init__(self, price, brand, camera):
        print('Inside phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera
# method overriding -> Polymorphism
    def buy(self):
        print('Buying a phone')
    
    # def return_phone(self):
    #     print('Returning a phone')

# class FeaturePhone(Phone):
#     pass
class SmartPhone(Phone):
    def buy(self):
        print('Buying a smartphone')
s = SmartPhone(2000, 'Apple', 13)
s.buy()