'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
for i in range(500):
    for j in range(500):
        for k in range(500):
            if pow(i,2) + pow(j,2) == pow(k,2)  and 0<i<j<k and i+j+k == 1000:
                print("{},{},{} ==> {}".format(i,j,k,i+j+k))
                print("product of {},{},{} is {}.".format(i,j,k,i*j*k))
                break


