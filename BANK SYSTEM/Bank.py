from database import *
import datetime
 
class Bank:
    
    def __init__(self,Username,account_number):
        self.__Username = Username
        self.__account_number = account_number
    
    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__Username}_transaction "
                 f"(timedate VARCHAR(30),"
                 f"account_number INTEGER ,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER)")
        
    def Balance_Enquiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE Username = '{self.__Username}';")
        print(f"{self.__Username} Balance is {temp[0][0]}")

    # ---------------- deposit ------------------
    def deposit(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE Username = '{self.__Username}';")
        test = amount + temp[0][0]
        db_query(f"UPDATE customers SET balance = '{test}' WHERE Username = '{self.__Username}';")
        self.Balance_Enquiry()

        db_query(f"INSERT INTO {self.__Username}_transaction VALUES("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f") ")
        
        print(f"{self.__Username} Amount is Sucessfully Depositted intO your Account {self.__account_number} ")

    # ---------------- withdraw ------------------
    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE Username = '{self.__Username}';")
        if amount > temp[0][0]:
            print("insufficient balance plece deposit money")
        else:
            test = temp[0][0] - amount 
            db_query(f"UPDATE customers SET balance = '{test}' WHERE Username = '{self.__Username}';")
            self.Balance_Enquiry()

            db_query(f"INSERT INTO {self.__Username}_transaction VALUES("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__account_number}',"
                    f"'Amount withdraw',"
                    f"'{amount}'"
                    f") ")
            
            print(f"{self.__Username} Amount is Sucessfully withdraw from your Account {self.__account_number} ")

    # ---------------- fundTransfer ------------------
    def fundTransfer(self, receive, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE Username = '{self.__Username}';")
        if amount > temp[0][0]:
            print("insufficient balance plece deposit money")
        else:
            temp2 = db_query(f"SELECT balance FROM customers WHERE account_number = '{receive}';")
            if not temp2:
                print("Receiver account not found")
                return

            test1 = temp[0][0] - amount
            test2 = amount + temp2[0][0]
            db_query(f"UPDATE customers SET balance = '{test1}' WHERE Username = '{self.__Username}';")
            db_query(f"UPDATE customers SET balance = '{test2}' WHERE account_number = '{receive}';")
            self.Balance_Enquiry()

            db_query(f"INSERT INTO {self.__Username}_transaction VALUES("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'fund transfer -> {receive}',"
                     f"'{amount}'"
                     f") ")

            # ensure receiver's transaction table exists then log for receiver
            temp_receiver = db_query(f"SELECT Username FROM customers WHERE account_number = '{receive}';")
            receiver_username = temp_receiver[0][0]
            db_query(f"CREATE TABLE IF NOT EXISTS {receiver_username}_transaction "
                     f"(timedate VARCHAR(30),"
                     f"account_number INTEGER ,"
                     f"remarks VARCHAR(30),"
                     f"amount INTEGER)")
            db_query(f"INSERT INTO {receiver_username}_transaction VALUES("
                     f"'{datetime.datetime.now()}',"
                     f"'{receive}',"
                     f"'fund received from {self.__Username}',"
                     f"'{amount}'"
                     f") ")

            print(f"{self.__Username} Amount is Sucessfully Transation from your Account {self.__account_number}")
