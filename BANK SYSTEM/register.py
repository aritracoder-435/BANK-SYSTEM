# user Registration Signin Signup
from database import *
from customer import *
from Bank import Bank
import random

# ---------------- PASSWORD SET FUNCTION ----------------
def set_password(min_length=6):    # default len is 6 
    while True:
        pwd = input("Enter a password: ")

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        has_space = " " in pwd   # 🔹 check for space

        special_chars = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"

        for ch in pwd:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special_chars:
                has_special = True

        pass_length = len(pwd) >= min_length

        if pass_length and has_upper and has_lower and has_digit and has_special and not has_space:
            print("🎉 Password set successfully.")
            return pwd   # exit loop when password is correct
        else:
            print("❌ Password is NOT valid.")
            print("   📌 Password must contain:")
            if not pass_length:
                print("    - At least 8 characters")
            if not has_upper:
                print("    - At least one uppercase letter")
            if not has_lower:
                print("    - At least one lowercase letter")
            if not has_digit:
                print("    - At least one digit")
            if not has_special:
                print("    - At least one special character (!@#$ etc.)")
            if has_space:
                print("    - No spaces allowed in the password")
            print("\n⚠ Please try again.\n")


#        -------- REGISTER --------
def signup():
    username = input("Create Usernmae: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username Already Exists")
        return signup()   # ✅ Added return to stop outer function after recursion
    else:
        Password = set_password()   # ✅ secure password setup
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
                print("Your Account Number: ", Account_number)
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
