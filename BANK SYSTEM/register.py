# user Registration Signin Signup
from database import *
from customer import *
from Bank import Bank
import random

#        -------- REGISTER --------

def signup():
    username = input("Create Usernmae: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username Already Exists")
        return signup()   # ✅ Added return to stop outer function after recursion
    else:
        Password = input("Enter your password: ")
        Name = input("Enter your nmae: ")
        Age = input("Enter your age: ")
        City = input("Enter your city: ")

        # Generate unique 8-digit account number
        while True:
            Account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT Account_number FROM customers WHERE Account_number = '{Account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number: ",Account_number)
                break

    cobj = customer(username, Password, Name, Age, City, Account_number)
    cobj.createuser()
    bobj = Bank(username, Account_number)
    bobj.create_transaction_table()


#        -------- LOGIN OR  SIGNIN --------
def signIn():
    Username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Check both username and password together
    temp = db_query(
        f"SELECT Username FROM customers WHERE Username = '{Username}' AND password = '{password}';"
    )

    if temp:
        print(f"Welcome {Username.capitalize()}! SignIn Successfully.")
        return Username
    else:
        print("Invalid Username or Password.")
        return signIn()
