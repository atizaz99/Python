class Customer:
    def __init__(self, name, age):
        self.name = name, 
        self.age = age
    def intro(self):
        print('I am ', self.name, 'and I am ', self.age)

c1 = Customer('A', 1)
c2 = Customer('B', 2)
c3 = Customer('C', 3)
L = [c1, c2, c3]
for c in L:
    c.intro()