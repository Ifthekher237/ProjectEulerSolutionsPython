'''
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''


def find_max(list):
    print("maximum  is {} ".format(max(list)))


def multiply_digits(slice):
    result=1
    for digit in slice:
        result=result*int(digit)
    print("{} = {} ".format(slice,result))
    return result

def extract_3_digit_number(string):
    list=[]
    i = 0
    count = 0
    while i < len(number_to_str):
        slice = number_to_str[i:i + 13]
        if len(slice) == 13:
            count += 1
            get_result=multiply_digits(slice)
            list.append(get_result)
        else:
            break
        i += 1
    find_max(list)
    print("total case {}.".format(count))


number=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
number_to_str=str(number)
print("total digit {}".format(len(number_to_str)))
extract_3_digit_number(number_to_str)
'''
the strateg i have used here is, first i have converted the total number into a string and secondly i have taken slice of adjacent 13 numbers
to take every adjacent 13 digits here i have used somethng like str[i:i+13]. the way it works is
let's take a number containing 10 digits ==> 1234567890
i=0 str[i:i+3] == str[0:3] == 123
i=1 str[i:i+3] == str[1:4] == 234
i=2 str[i:i+3] == str[2:5] == 345
... and so on
every time a slice is taken then it is passed to a function to multiply the digits that are contained in that slice.
then the multiplicatio result is returned and appended into a list
finally the whole list is passed into anothr functio to find the maximum multiplication result.
and that's it !!
'''
