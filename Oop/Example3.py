class A:
    def __init__(self):
        self.var1 = 100
    def display(self, var1):
        print('Class A',self.var1)



class B(A):
    def display2(self, var1):
        print('Class B',self.var1)

# object create
obj = B()
obj.display(200)