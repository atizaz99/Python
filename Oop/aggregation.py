class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)
class address:
    def __init__(self, city, state, zip):
        self.city =city
        self.state = state
        self.zip = zip
    def change_address(self,new_city, new_pin, new_state):
        self.city = new_city
        self.zip = new_pin
        self.state = new_state


add = address('A', 111, 'b')
cust = Customer('Nitish', 'Male',  add)
cust.edit_profile('Ali','b', 11, 'h')

print(cust.address.zip)