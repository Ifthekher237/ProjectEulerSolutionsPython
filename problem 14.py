"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

dicti = {}  # keys of the dictionary are the values of i and corresponding values are length of chain.
i = 13

# outer while loop increase the value of i and inner while loop
# produces the collatz sequence
while i <= 1000000:
    n = i
    count = 1              # here counting starts from 1 because whenever n becomes 1, the inner while loop(where count
    while n != 1:          # variable is increasing) won't be executed anymore. so if we didn't
        count += 1         #  start from 1, n would always be less 1 than the actual count.
        if n % 2 != 0:     # check whether the number is odd or even
            n = (3 * n) + 1
        else:
            n = (n / 2)
    dicti[i] = count
    i += 1

maximum = max(dicti.values())     # find the maximum value in the dictionary values and then using for loop finding
                                  # corresponding dictionary key...
for i in range(13, 1000001):
    if dicti[i] == maximum:
        print(i, maximum)
