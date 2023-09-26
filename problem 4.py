'''
A palindromic number reads the same both ways.
 The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(n):
    number_to_string = str(n)
    new_string = ""
    i = -1
    while i >= -len(number_to_string):
        new_string = new_string + number_to_string[i]
        i -= 1
    #print("number:{} - reversed number:{}.".format(number_to_string,new_string))
    if new_string == number_to_string:
        return int(new_string)
    else:
        return 0



total=0
palindrome_number_list=[]
for i in range(100,1000):
    for j in range(100,1000):
        total+=1
        product=i*j
        palindrome_number=is_palindrome(product)
        if palindrome_number > 0:
            palindrome_number_list.append(palindrome_number)
print("total number:{}".format(total))
print(max(palindrome_number_list))