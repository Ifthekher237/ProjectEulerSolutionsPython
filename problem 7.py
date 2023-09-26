'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''


def is_prime(n):
    count=0
    for i in range(1,int(pow(n,.5))+1):
        if n%i == 0: count+=1
    if count == 1 :
        print(n)
    if count == 1 :
        return True
    else:
        return False

total_prime=10001
i=2
while total_prime > 0:
    get_result=is_prime(i)
    if get_result == True:
        total_prime-=1
    else:
        total_prime=total_prime
    i+=1




