'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

#the program is not completed yet. Here still i have to multiply few things in hand like divisor at every step and final line at last step.
def check_divisiblity(list, i):
    count = 0
    for ele in list:
        if ele % i == 0: count += 1
    return count                                                                       #the flowchart i have followed here ==>
                                                                          #1. take a list
                                                                          #2.pass it to multiple() function
def multiple(list):                                                       #3.find a factor for the list which divides at least 2 entry. To do that, here another function check_divisibility()
    print("multiple() function is called with {}".format(list))           #4 function is called.
                                                                          #5.if count>1, update the list.
    for i in range(2, int(max(list))):                                    #6.and call the multiple() recursively with updated list and then again perform step 3,4,5 step.
        count = check_divisiblity(list, i)                                #7.if count<=1 then increase i and go to step 3

        if count > 1:
            print("the list {} is divided by ==> {}".format(list, i))
            for j in range(len(list)):
                if list[j] % i == 0:
                    list[j] = list[j] / i
            multiple(list)
        else:
            continue
    return list


list = []
i = 0
total_input = int(input("How many number do you want to input:"))
print("Enter your numbers:\n")
while i < total_input:
    get_number = int(input())
    list.append(get_number)
    i += 1

print(multiple(list))

