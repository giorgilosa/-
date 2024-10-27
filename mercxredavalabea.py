#############
# task1
######################
int_list = [10, 20, 30, 40]

def add_to_list(number):
    global int_list
    int_list.append(number)
    return int_list

add_to_list(50)
print(int_list)

#############
# task2
######################

def sum(number):
    if number > 8:
        return 0
    else:
        return number + sum(number + 1)

result = sum(4)
print(f"The sum is: {result}")



########################
#task3
###############################

def reverse_string(s, index=0):
    if index == len(s):
        return ""
    else:
        return reverse_string(s, index + 1) + s[index]

if __name__ == "__main__":
    input_string = "Giorgi"
    result = reverse_string(input_string)
    print("Input:", input_string, "Output:", result)


########################
#task4
###############################
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def generate_fibonacci_sequence(terms):
    sequence = []
    for i in range(terms):
        sequence.append(fibonacci(i))
    return sequence


fibonacci_sequence = generate_fibonacci_sequence(9)
print(fibonacci_sequence)
