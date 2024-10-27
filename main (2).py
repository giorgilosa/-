########################################################
# task 1
########################################################
num = int(input("Enter the number: "))
print(num)
while num > 0:

    print(num)
    num -=1


########################################################
# task 2
########################################################
total_sum = 0

while True:
     section = input("Enter the number or type sum: ")
     if section == "sum" :
         print(total_sum)
         break
     elif int(section) > 0:
         total_sum += int(section)
     else:
         print("Enter the correct number: ")

########################################################
# task 3
########################################################




import random


secret_number = random.randint(1, 10)
print(secret_number)
lives = 5

print("Welcome! Try to guess the random number between 1 and 10.")

while lives > 0:
    guess = int(input("Enter your guess: "))


    if secret_number == guess:
        print("Correct")

    if guess > secret_number:
        print("Your guess is too high: ")
    elif guess < secret_number:
        print("Your guess is too low: ")
    else:
        break


    lives -= 1



