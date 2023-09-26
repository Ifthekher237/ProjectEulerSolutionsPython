'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''



def find_prime(n):
    count=0
    for i in range(1,int(pow(n,.5))+1):
        if n%i == 0: count+=1
    if count == 1:
        return n
    else:
        return 0



sum=0
for number in range(2,2000000):
    get_prime=find_prime(number)
    sum+=get_prime
print("sum of all prime number below 2000000) is {}".format(sum))














