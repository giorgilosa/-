# ##########################################################
# Task 1
#
# #########################################################

number = int(input("Enter a number:"))
if number % 2 == 0:
   print("even")
else:
   print("odd")

# ##########################################################
# Task 2
#
# #########################################################

text = input("Enter a text: ")

words_to_search = ["small", "tall", "middle"]

found = False

for word in words_to_search:
    if word in text:
       print(word)
       found = True
if not found:
   print("None of the words 'small', 'tall', or 'middle' are found in the text.")

# ##########################################################
# Task 3
#
# #########################################################

first_number = float(input("Enter the first number: "))


second_number = float(input("Enter the second number: "))


operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
   result = first_number + second_number
elif operator == '-':
   result = first_number - second_number
elif operator == '*':
   result = first_number * second_number
elif operator == '/':
   if second_number != 0:
      result = first_number / second_number
   else:
       result = "Error: Division by zero is not allowed."
else:
   result = "Error: Invalid operator."

print("Result:", result)





