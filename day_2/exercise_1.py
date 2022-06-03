'''Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8'''

numImput = str(input('write a number'))

numList = [int(i) for i in str(numImput)]


sum = 0
for i in numList:
    sum += i

print(sum)
