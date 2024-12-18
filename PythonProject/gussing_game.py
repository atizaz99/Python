import random as rd
n = rd.randrange(1, 10)
guess = int(input('Enter your number 1 to 10 : '))

while n != guess:
    
    
    if guess < n:
        print('Number is small')
        guess = int(input('Enter your number 1 to 10 : '))
    if guess > n:
        print('Number is large')
        guess = int(input('Enter your number 1 to 10 : '))
    else:
        break
print('Number is correct')
