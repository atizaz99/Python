class ATM:
    # Function Vs Methods
    # method is written inside of a class whereas functio is written outside of class
    # Constractor 
    # special/magic/dunder methods
    ''' Use of constructor
    constructor is a special method in python which is used to initialize the state of an object.
    It is called when an object is created from a class and it allows the class to initialize the
    attributes of the class.
    it's control not in hand of user.
    Configuration related task.
    to connect database.

    
    '''
    '''
    self: 
    self is a reference to the current instance of the class and is used to access variables and methods from the class.
    It is used to access the attributes and methods of the class.
    '''
    def __init__(self):
        self.pin = ''
        self.balance = 0

        self.menu()
        # print('class is Created')
    def menu(self):
        user_input = input('''
        Hello, how would you like proceed
        1. Enter 1 to create pin
        2. Enter 2 to deposit 
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit 
        ''')
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print('Bye')
    def create_pin(self):
        self.pin = input('Enter your pin')
        print('Pin created')
    def deposit(self):
        temp = input('Enter you pin ')
        if temp == self.pin:
            amount = int(input('Enter the amount'))
            self.balance = self.balance+amount
            print('Deposit successful')
        else:
            print('Invalid Pin')
    def withdraw(self):
        temp = input('Enter you pin ')
        if temp == self.pin:
            amount = int(input('Enter the amount'))
            if amount <self.balance:
                self.balance = self.balance - amount
                print('Operatio Successfull')
            else:
                print('Insufficient fund')

        else:
            print('Invalid pin')
    def check_balance(self):
        temp = input('Enter you pin ')
        if temp == self.pin:
            print('Your balance is', self.balance)
        else:
            print('Invalid pin')


atm = ATM()