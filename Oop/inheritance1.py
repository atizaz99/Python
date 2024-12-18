class user:
    def login(self):
        print('login')
    def register(self):
        print('register')

class Student(user):
    def enroll(self):
        print('enroll')
    def review(self):
        print('review')
    
stud1 = Student()
stud1.login() # login
stud1.register() # register
stud1.enroll() # enroll
stud1.review() # review