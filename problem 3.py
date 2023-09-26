'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


def is_prime(factor):
    count=0
    end=int(pow(factor, .5))
    for j in range(1,end+1):
        if factor%j == 0:
            count+=1
    if count ==1  : print(factor)

def factor(n):
    if n == 1:
        return 1
    else:
        for i in range(2,n+1):              # here you must use (n+1) otherwise error arise.(figure out why)
            if n%i == 0 :
                print("{}".format(i))
                fact=i*factor(int(n/i))     #  (n/i) is a float number, a float number can't be used inside range() function so we have to conver float into int before we use it in range() function.
                return fact                  #try not using this line and see what error occurs and try to figure out why that error occurs

print("prime factors are::")
factor(3628800)                                 #calling factors() functon to get  all factors of a given value.


#warining!!
#if we append every factor of n into a list and then pass it to is_prime() function, for a smaller value
#you will easily get the answer but value like 600851475143, it will take mauch longer time. That's why
 #every time a factor is found it is passed to the function.

