# # Set
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print(house)

# # Set
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# houses = set()
# for student in students:
#     if student["house"] not in houses:
#         houses.add(student["house"])

# for house in sorted(houses):
#     print(house)

# # Global variables
# balance = 0
# def main():
#     print("Balance: ", balance)

# if __name__ == "__main__":
#     main()


# # Global variables
# # we can not run this program because of local varible
# balance = 0
# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)
# # you can not assign global variable in your function
# def deposit(n):
#     balance += n

# def withdraw(n):
#     balance -= n 

# if __name__ == "__main__":
#     main()


# # Global variables
# # Now adding global keyword before the varible, it can take varible as global varible 
# balance = 0
# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)
# # you can now assign the varible in your function
# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n 

# if __name__ == "__main__":
#     main()

# # modify our code to use a class instead of global variable
# class Account():
#     def __init__(self):
#         self._balance = 0
    
#     @property
#     def balance(self):
#         return self._balance
    
#     def deposit(self, n):
#         self._balance += n
    
#     def withdraw(self, n):
#         self._balance -= n

# def main():
#     account = Account()
#     print("Balance: ", account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balance: ",account.balance)

# if __name__ == "__main__":
#     main()


