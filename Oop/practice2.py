class Parent:
    def __init__(self, num):
        self.__num = num
    def ger_num(self):
        return self.__num


class Child(Parent):
    def show(self):
        print('This is in child class')
    
son = Child(100)
print(son.ger_num())
son.show()