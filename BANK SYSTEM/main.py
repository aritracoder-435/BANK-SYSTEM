from register import *
from Bank import *
status = False
import shutil   # used for terminal width

# ------- Heading function ----------
def print_app_title():
    title = " 🪙  B A N K I N G   S Y S T E M  🪙 "
    border = "═" * (len(title) + 4)
    term_width = shutil.get_terminal_size().columns

    top = f"╔{border}╗"
    mid = f"║  {title}  ║"
    bottom = f"╚{border}╝"

    def center_line(line):
        return line.center(term_width)

    print("\n" * 1)
    print(center_line(top))
    print(center_line(mid))
    print(center_line(bottom))
    print("\n")


# ------- Goodbye message ----------
def goodbye_message(user=None):
    print("\n" + "═" * 60)
    if user:
        print(f" 🙏 Thank you, {user.capitalize()}! Visit Again. 🙏")
    print(" Developed with ❤️  by  Aritra Mandal")
    print("═" * 60 + "\n")


# ---------- main loop (fixed) -----------
print_app_title()
while True:
    try:
        register = int(input("\n--- MAIN MENU ---\n"
                             "1️⃣  SignUp\n"
                             "2️⃣  SignIn\n"
                             "3️⃣  Exit\n"
                             "Choose an option (1/2/3): "))

        if register == 1:
            signup()
        elif register == 2:
            user = signIn()
            status = True
            break
        elif register == 3:
            print("═" * 60)
            print("👋 Thank you for visiting our Banking System!")
            print("Developed with ❤️  by  Aritra Mandal")
            print("═" * 60 + "\n")
            exit()
        else:
            print("⚠️  Please enter a valid option from the menu.")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")


# fetch account number (do not print it)
account_number = db_query(f"SELECT account_number FROM customers WHERE Username = '{user}';")

# ---------- logged-in menu ----------
while status:
    print(f"\n \t✨ Welcome {user.capitalize()}! Choose your Banking Service ✨\n")

    try:
        facility = int(input("\n[ --- BANK SERVICES --- ]\n"
                             "1️⃣  Balance Enquiry\n"
                             "2️⃣  Cash Deposit\n"
                             "3️⃣  Cash Withdraw\n"
                             "4️⃣  Fund Transfer\n"
                             "5️⃣  Exit\n"
                             "Choose an option (1/2/3/4/5): "))

        if 1 <= facility <= 5:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.Balance_Enquiry()

            elif facility == 2:
                while True:
                    try:
                        amount = int(input("💰 Enter amount to deposit: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        # status = False
                        print(f"✅ Successfully deposited ₹{amount}!")
                        break
                    except ValueError:
                        print("❌ Please enter a valid number.")

            elif facility == 3:
                while True:
                    try:
                        amount = int(input("💸 Enter amount to withdraw: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        # status = False
                        print(f"✅ Successfully withdrawn ₹{amount}!")
                        break
                    except ValueError:
                        print("❌ Please enter a valid number.")

            elif facility == 4:
                while True:
                    try:
                        receive = int(input("🏦 Enter receiver's account number: "))
                        amount = int(input("💵 Enter amount to transfer: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundTransfer(receive, amount)
                        mydb.commit()
                        # status = False
                        print(f"✅ Successfully transferred ₹{amount} to account {receive}!")
                        break
                    except ValueError:
                        print("❌ Invalid input! Please enter numbers only.")
                        continue

            elif facility == 5:
                goodbye_message(user)
                exit()

        else:
            print("⚠️  Please enter a valid option from the menu.")

    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")
        continue
