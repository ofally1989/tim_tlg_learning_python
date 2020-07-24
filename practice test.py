# What are the two primary number types in python?- integers and floating points.
# integer
pi = 3.14
radius = 4
print(float(pi * radius **2))
name = 'Tim'
surname = "O'Fallon"
#string
print(name + ' ' + surname)
print(name.lower() + ' ' + surname.upper())

question = input('Is basic training difficult? y/n: ')
if question == 'y':
    print('You\'re in the Navy aren\'t you? ')
else:
    print('You must have been in the Air Force. ')

budget = float(input('What is your monthly budget? '))
if budget >= 1001:
    print('Error, you\'ll be fine ')
elif budget > 550:
    print('You will eat fine this month! ')
elif budget >= 550:
    print('This is the average American food budget. ' )
elif budget <= 0:
    print('Error, this is not a valid entry. ')
else:
    print('This is less than the average American food budget. ')


x = 0
while x <= 100:
    print(x)
    x = x + 2



for i in range(2, 100, 2):
    print(i)

nums = []

import random
z = random.randint(1,100)
print(z)


nums = []
import random
x = random.randint(1,100)

for x in range(100):
    nums.append(random.randint(1,100))
print(nums)








