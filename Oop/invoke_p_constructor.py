class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, ram, storage):
        print('First here')
        super().__init__(price, brand, camera)
        self.ram = ram
        self.storage = storage
        print('Inside smart phone constructor')


s = SmartPhone(2000, 'samsung', 12, 'Adroid', 2)
print(s.ram)
print(s.brand)
        