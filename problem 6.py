'''
The sum of the squares of the first ten natural numbers is,
12+22+...+102=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
'''






squared_sum=0
sum=0
for i in range(101):
    sum+=i
    squared_sum+=(i*i)
square_of_sum=pow(sum,2)
print("The sum of the squares of the first ten naturan number is {}.".format(squared_sum))
print("The square of the sum of the first ten natural numbers is {}.".format(square_of_sum))
print("the difference between the sum of the squares of the first ten natural numbers and the square of the sum is {}".format(square_of_sum-squared_sum))
