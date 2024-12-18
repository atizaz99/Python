class Customer:
    def __init__(self, name):
        self.name = name
def greet(customer):
    print(id(customer))
    customer.name = 'Atizaz'
    print(customer.name)
    print(id(customer))


cust = Customer('Ali')
print(id(cust))
greet(cust)
print(cust.name)
# class object are also mutable like list dict and set

