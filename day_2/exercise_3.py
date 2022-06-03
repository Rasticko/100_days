'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
'''


age = input('Enter your age: ')

try:
    age = int(age)
    years_left = 90 - age
    z = years_left * 12
    y = years_left * 52
    x = years_left * 365
    print(f'You have {x} days, {y} weeks, and {z} months left')

except ValueError:
    print('You need to enter an int')
