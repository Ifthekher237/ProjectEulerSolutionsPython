"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
 (there is a picture, see it from here ==> https://projecteuler.net/problem=15
How many such routes are there through a 20×20 grid?
"""


# first we are considering it as an n by n matrix and starting its indexing from(0, 0)
# then we will take row and column number of destination cell .

def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1


print("dimension of your matrix will be 1 more than the number of grid(e.g. if you have 2 * 2 grid "
      "then dimension of your matrix is 3 * 3)")

dimension_of_matrix = int(input("\nEnter the dimension of the marix :: "))
p = int(input("Enter the row number of your destination cell(indexing starts from (0, 0)) :: "))
q = int(input("Enter the column number of your destination cell(indexing starts from (0, 0)) :: "))

n = p + q
m = q

total_path = (fact(n)) / (fact(n - m) * fact(m))
print(total_path)

"""
# dimension of your matrix will be 1 more than the number of grid(e.g. if you have 2 * 2 grid 
# then dimension of your matrix is 3 * 3)

h = 21  # row
w = 21   # col

matrix = [[0 for x in range(w)] for y in range(h)] # creating a zero matrix which will be updated later

for i in range(h):
    for j in range(w):
        print(matrix[i][j], end = " ")
    print()

print()

for i in range(h):
    for j in range(w):
        if i == 0 or j == 0 :
            matrix[i][j] = 1
        print(matrix[i][j], end = " ")
    print()

print()

for i in range(1,h):
    for j in range(1, w):
        matrix[i][j] = matrix[i][j-1] + matrix[i - 1][j]
    print()
print()

print(matrix[h - 1][w - 1])  

#for i in range(h):
#    for j in range(w):
#        print(matrix[i][j], end = " ")
#    print()


"""
