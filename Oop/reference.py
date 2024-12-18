class Customer:
    def __init__(self, name, gender):

        self.name = name
        self.gender = gender
'''
pass by reference:
call the function and pass the object of class.
the id will be same.
if you pass value to a function the it will edit the object than the orignal object will also change.


'''

def greet(customer):
    if customer.gender =='male':
        print('Hello', customer.name, 'Sir')
    else:
        print('Hello', customer.name, 'Madam')
    # returning the function
    cust2 = Customer('Kazim', 'male')
    return cust2
cust = Customer('Ali', 'male') 
greet(cust)
obj = Customer('fatima', 'female')
greet(obj)
new_cusotmer = greet(cust)
print(new_cusotmer.name)
