############################
# task 1
###########################

def are_anagrams(str1, str2):

    return sorted(str1) == sorted(str2)


print(are_anagrams("earth", "heart"))
print(are_anagrams("apple", "pale"))
print(are_anagrams("triangle", "integral"))

############################
# task 2
###########################

def count_char_occurrences(string, char):

    return string.count(char)


print(count_char_occurrences("It is a world", "o"))
print(count_char_occurrences("apple pie", "p"))
print(count_char_occurrences("python programming", "n"))
print(count_char_occurrences("openai", "a"))



############################
# task 3
###########################

def fibonacci_sequence(n):

    fib_sequence = []


    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence



print(fibonacci_sequence(14))
print(fibonacci_sequence(7))
print(fibonacci_sequence(1))
print(fibonacci_sequence(2))