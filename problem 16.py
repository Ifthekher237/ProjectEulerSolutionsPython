"""

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

result = 1                      # this problem can be solved without using loop. just using pow() function.
for i in range(1, 1001):
    result *= 2

#print(result)

sum = 0
for digit in str(result):
    sum += int(digit)

print("sum of all digits of the number 2^{power} is {sum}".format(power = 1000, sum = sum))