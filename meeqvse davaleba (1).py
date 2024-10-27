
##########
# task1
#########################################


text = input('Please enter the sentence: ')
print(text)
words = text.lower().split()
cnt = {}
for word in words:
    if word in cnt:
        cnt[word] += 1
    else:
        cnt[word] = 1

print(cnt)


##########
# task2
#########################################


number1 = float(input("Enter the 1st number: "))
operator = input("Enter an operator (+, -, *, /): ")
number2 = float(input("Enter the 2nd number: "))

oprts = {
    '+': number1 + number2,
    '-': number1 - number2,
    '*': number1 * number2,
    '/': number1 / number2 if number2 != 0 else "Can't divide by zero"
}

if operator in oprts:
    result = oprts[operator]
else:
    result = 'Faulty operator!'

print(f"Result: {result}")


####################
# task3
#########################################


squares = {}
for x in range(1, 11):
    squares[x] = x ** 2

print(squares)

####################
# task4
#########################################

company = {
    'Finance': [
        {'first_name': 'Eve', 'last_name': 'Davis', 'age': 29, 'salary': 4800},
        {'first_name': 'Frank', 'last_name': 'Miller', 'age': 45, 'salary': 5300}
    ],
    'Marketing': [
        {'first_name': 'Grace', 'last_name': 'Taylor', 'age': 32, 'salary': 5700},
        {'first_name': 'Henry', 'last_name': 'Anderson', 'age': 38, 'salary': 5900}
    ]
}

for comp, staff in company.items():
    total_salary = 0
    employee_count = 0


    for employee in staff:
        total_salary += employee['salary']
        employee_count += 1

    average_Sal = total_salary / employee_count
    print(f"Average salary in {comp}: {average_Sal}")