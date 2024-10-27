##########################################
# task 1
################

my_list = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]


third_element = my_list[2]
ninth_element = my_list[8]
fourteenth_element = my_list[13]

result = third_element + ninth_element + fourteenth_element

print(result)


##########################################
# task 2
# #######################################


import random

random_list = [random.randint(1, 80) for _ in range(20)]

odd_num = [num for num in random_list if num % 2 != 0]

if odd_num:  # Check if the list is not empty
    smallest = odd_num[0]
    largest = odd_num[0]

    for num in odd_num:
        if num < smallest:
            smallest = num
        if num > largest:
            highest = num

    print("Odd values:", odd_num)
    print("Smallest odd :", smallest)
    print("Highest odd :", largest)
else:
    print("The list does not contain any odd values.")



##########################################
# task 3
################


my_llist = [43, '22', 12, 66, 210, ["hi"]]


index_of_210 = my_llist.index(210)
print("Index of 210:", index_of_210)

my_llist[5].append("hello")

my_llist.remove(my_llist[2])
print("List after removing element at index 2:", my_llist)

my_llist_2 = my_llist.copy()
my_llist_2.clear()

print("my_llist:", my_llist)
print("my_llist_2:", my_llist_2)




##########################################
# task 4
################


matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
    raise ValueError("Matrices must have the same dimensions")


result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]


for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]


print("Sum of the two matrices:")
for row in result:
    print(row)



#######################################
#task 5
###########################################

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        transposed[j][i] = matrix[i][j]

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in transposed:
    print(row)



#######################################
#task 6
###########################################

import random

random_matrix_1 = [[random.randint(1, 50) for _ in range(4)] for _ in range(4)]

# Print the matrix
print("Matrix random_matrix_1:")
for row in random_matrix_1:
    print(row)




