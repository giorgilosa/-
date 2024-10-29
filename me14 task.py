
# task1
##################

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder} successfully deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Please enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} has withdrawn ${amount:.2f}. Remaining balance: ${self.balance:.2f}.")
        elif amount > self.balance:
            print(f"{self.account_holder}, you don't have enough funds for this withdrawal.")
        else:
            print("The withdrawal amount must be a positive value.")

    def check_balance(self):
        print(f"{self.account_holder}, your current balance is: ${self.balance:.2f}")

account1 = BankAccount("345678", "Oliver Twist")
account2 = BankAccount("890123", "Liam Johnson")

account1.deposit(1500)
account1.withdraw(200)
account1.check_balance()

account2.deposit(3000)
account2.withdraw(500)
account2.withdraw(3000)
account2.check_balance()

print(f"Final balance for {account1.account_holder}: ${account1.balance:.2f}")
print(f"Final balance for {account2.account_holder}: ${account2.balance:.2f}")


print(f"Final balance for {account1.account_holder}: ${account1.balance:.2f}")
print(f"Final balance for {account2.account_holder}: ${account2.balance:.2f}")

##################
# task2
##################

class Student:
    def __init__(self, full_name, student_id):
        self.full_name = full_name
        self.student_id = student_id
        self.courses = []

    def register_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.full_name} has been registered for {course}.")
        else:
            print(f"{self.full_name} is already registered for {course}.")

    def show_info(self):
        print(f"Name: {self.full_name}")
        print(f"ID: {self.student_id}")
        print("Courses enrolled:", ', '.join(self.courses) if self.courses else "No courses registered.")

student3 = Student("Evelyn Smith", "S201")
student4 = Student("Max Taylor", "S202")

student3.register_course("History")
student3.register_course("Literature")
student4.register_course("Mathematics")
student4.register_course("Computer Science")
student4.register_course("Mathematics")

student3.show_info()
student4.show_info()

