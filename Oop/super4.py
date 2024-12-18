class Parent:
    def __init__(self):
        self.__num = 100
    def show(self):
        print('Parent', self.__num)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 200

    def show(self):
        # print(self.num)
        print('Child',self.__var) 
p = Parent()
p.show()
s = Child()
s.show()
