class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length
    
    def peri(self):
        return 2 * (self.width + self.length)

rect1 = Rectangle(40, 40)
print("rect1 area: ", rect1.area())
print("rect1 peri: ", rect1.peri())

rect2 = Rectangle(20, 30)
print("rect2 area: ", rect2.area())
print("rect2 peri: ", rect2.peri())


class BankAccount:
    def __init__(self,numb, sum):
        self.account_number = numb
        self.balance = sum
        print(f"зачислено:{sum}")
    
    def add(self, sum):
        self.balance = self.balance + sum
        print(f"зачислено:{sum}")

    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance = self.balance - sum
            print(f"Со счета снято: {sum}")
        else:
            print("Недостаточно средств на счете")

acc1 = BankAccount("123456577", 1000)
acc1.add(200)
acc1.withdraw(500)
acc1.withdraw(300)
acc1.withdraw(900)