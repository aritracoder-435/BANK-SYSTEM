import pandas as pd
import os
import json
import time
import threading
import sys
import shutil
import time

#------------------- title part -----------------
def print_app_title():
    title = " BANK SYSTEM "
    border = "═" * (len(title) + 4)
    
    # get terminal width
    term_width = shutil.get_terminal_size().columns
    
    # build lines
    top = f"╔{border}╗"
    mid = f"║  {title}  ║"
    bottom = f"╚{border}╝"    
    
    # calculate padding for center
    def center_line(line):
        return line.center(term_width)
    
    print("\n" * 1)   # some top spacing
    print(center_line(top))
    print(center_line(mid))
    print(center_line(bottom))
    print("\n")


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
            print("🎉 Password successfully.")
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


# ---------------- USER HANDLING ----------------

# 🆕 Option 4: Improved JSON error handling
def load_users():
    if os.path.exists("dataBase.json"):
        try:
            with open("dataBase.json", "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠ Database corrupted. Creating a new one.")
            return []
    return []


def save_users(users):
    with open("dataBase.json", "w") as f:
        json.dump(users, f, indent=4)


# ---------------- CLEAR FUNCTION ----------------
def clear_ter():
    os.system('cls' if os.name == 'nt' else 'clear')  # this is for clear terminal


# 🆕 Option 3: Loading animation helper function
def loading_animation(text="Loading", delay=0.5, repeat=3):
    for i in range(repeat):
        print(f"{text}" + "." * i, end="\r")
        time.sleep(delay)
    print(" " * 20, end="\r")  # clear line


# 🆕 Option 6: User dashboard after login
def user_dashboard(username):
    while True:
        clear_ter()             # clear old content
        print_app_title()       # 🆕 show title always
        print(f"\n👋 Welcome, {username}!\n🙂")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print("💰 Your balance feature coming soon.")
        elif choice == "2":
            print("💸 Deposit feature coming soon.")
        elif choice == "3":
            print("🏧 Withdraw feature coming soon.")
        elif choice == "4":
            print("👋 Logging out...")
            loading_animation("Logging out")
            clear_ter()  # clear dashboard when logging out
            break
        else:
            print("❌ Invalid choice, try again.")


#  ------------REGISTER PART-----------------
def register_user():
    clear_ter()           # 🆕 clear previous content
    print_app_title()     # 🆕 show title
    print("\n--- Register your new account ---")
    users = load_users()

    while True:   # keep asking until unique username
        username = input("Enter username: ")

        # check if username already exists
        if any(user["username"] == username for user in users):
            print("❌ This username already exists. Try another one.\n")
        else:
            break   # ✅ unique username found

    password = set_password()   # ✅ this will return the password

    # Add new user
    user_data = {"username": username, "password": password}
    users.append(user_data)
    save_users(users)
    print(user_data)
    print(f"✅ User '{username}' registered successfully!")

    # 🆕 Option 3: Loading animation after registration
    loading_animation("Saving data")


#  ------------LOGIN PART-------------------
def login_user():
    while True:
        clear_ter()
        print_app_title()
        print("\n--- Login your account ---")
        users = load_users()
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("🎉 Login successful! \n")
                loading_animation("Loading")
                clear_ter()
                user_dashboard(username)
                return True

        print("❌ Invalid username or password.")
        input("Press Enter to try again...")  # wait so user sees the message



# ---------------- MAIN MENU ----------------
def main_menu():
    while True:
        clear_ter()
        print_app_title()
        print("\n--- MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose option (1/2/3): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            success = login_user()   # call login_user
            if success:              # only clear if login successful
                clear_ter()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main_menu()
