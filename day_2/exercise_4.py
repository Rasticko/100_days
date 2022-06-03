# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

tip = 1.12

try:
    bill = float(input('What is the bill ammount?: '))
    people = int(input('How many people are splitting the bill?: '))
    bill_split = (bill/people) * tip
    print(f'Each person has to pay ${round(bill_split, 2)}')

except ValueError:
    print('Float or int error')

