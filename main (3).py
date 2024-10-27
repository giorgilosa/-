##########################################
# task 1
##########################################

def is_palindrome(text):
    cleaned_text = ''.join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]

user_input = input("Enter some text: ")

if is_palindrome(user_input):
    print("The text entered is a palindrome.")
else:
    print("The text entered is not a palindrome.")


##########################################
# task 2 
##########################################
user_input = input("Enter some text: ")
ascii_values = ' '.join(str(ord(char)) for char in user_input)
print("The ASCII values are:", ascii_values)








