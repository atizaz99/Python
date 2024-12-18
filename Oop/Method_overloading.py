class Geometry:
    def area(self, a, b=0):
        if b ==0:
            print('Circle', 3.14*a*a)
        else:
            print('Rec', a*b)
        
    
    # def area(self, l, b):
    #     return l*b
    

obj = Geometry()
obj.area(4, 2)
