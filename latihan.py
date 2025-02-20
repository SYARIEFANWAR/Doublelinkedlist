# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount >= 0:
#             self.__balance += amount 
#         else:
#             print("Invalid deposit amount. Please enter a positive amount.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#         else:    
#             print("Invalid withdrawal amount or insufficient balance.")

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)
# print("Current balance:", account.get_balance())

# class User:
#     def __init__(self, password):
#             self.__password = password

#     def set_password(self):
#         new_password = input("Enter a new password: ")
#         if len(new_password) >= 8:
#             self.__password = new_password
#         else:           
#             print("Password must be at least 8 characters long.")  
    
#     def check_password(self):
#         password = input("Enter your password: ")
#         if password == self.__password:
#             print("Access granted")
#         else:
#             print("Access denied")

# user = User("password")
# user.set_password()
# user.check_password()

class Sensor:
    def __init__(self, temperature):
        self.__temperature = temperature
    
    def set_temperature(self):
        new_temperature = float(input("Enter a new temperature: "))
        if -10 <= new_temperature <= 100:
            self.__temperature = new_temperature
        else:   
            print("Temperature must be between -10 and 100 degrees.")
    
    def get_temperature(self):
        return self.__temperature   
kapal = Sensor(25.0)
kapal.set_temperature()
print(kapal.get_temperature())