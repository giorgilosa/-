
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"{self.name}: Deposit = {self.deposit}, Loan = {self.loan}"


class House:
    def __init__(self, id, price, owner):
        self.id = id
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def sell(self, buyer, loan_amount=0):
        if loan_amount:
            self.status = "sold on loan"
            buyer.loan += loan_amount
            buyer.deposit -= (self.price - loan_amount)
            print(f"{self.id} sold to {buyer.name} with a loan of {loan_amount}. Status: {self.status}")
        else:
            self.status = "sold"
            buyer.deposit -= self.price
            print(f"{self.id} sold to {buyer.name}. Status: {self.status}")

        self.owner.deposit += self.price
        self.owner = buyer

    def __str__(self):
        return f"House {self.id}: Price = {self.price}, Owner = {self.owner.name}, Status = {self.status}"


buyer = Person("Lana")
seller = Person("Ana")

print(seller)
print(buyer)

house = House(id="555555", price=8500, owner=seller)
print(house)

house.sell(buyer)
print(seller)
print(buyer)
print(house)

house.sell(buyer, loan_amount=4000)
print(seller)
print(buyer)
print(house)


