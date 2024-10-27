#########################################
# task 1
#########################################

def mint(list1, list2):
    return list(zip(list1, list2))


params1 = [1, 2, 3]
params2 = ['a', 'b', 'c']

result = mint(params1, params2)
print(result)

#########################################
# task 2
#########################################

even_elements = lambda lst: [x for x in lst if x % 2 == 0]


params = [1, 2, 3, 4, 5, 6, 7]

result = even_elements(params)
print(result)

#########################################
# task 3
#########################################


positive_nums = lambda values: list(filter(lambda n: n > 0, values))


numbers_list_1 = [-10, 15, 0, 22, -3, 7]

result_1 = positive_nums(numbers_list_1)
print(result_1)

#########################################
# task 4
#########################################

check_palindromes = lambda lst: list(filter(lambda x: x == x[::-1], lst))


words = ["madam", "apple", "racecar", "banana", "level"]

result = check_palindromes(words)
print(result)
Lambda function to filter palindromes from the list

#########################################
# task 5
#########################################

from functools import reduce


def multiply_elements(numbers):
    return reduce(lambda x, y: x * y, numbers)


params = [1, 2, 3, 4, 5]
result = multiply_elements(params)
print(result)

#########################################
# task 6
#########################################


def filter_by_ending(string_list, ending):
    try:

        return list(filter(lambda x: isinstance(x, str) and x.endswith(ending), string_list))
    except TypeError:
        return "Invalid input! Please provide a list of strings and a string ending."


params = ['hello', 'world', 'coding', 'nod']
ending = 'ing'

result = filter_by_ending(params, ending)
print(result)




