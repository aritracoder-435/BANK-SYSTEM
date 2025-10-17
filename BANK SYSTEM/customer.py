# customer details
from database import *

class customer:
    def __init__(self, Username, Password, Name, Age, City, Account_number):
        self.__Username = Username
        self.__Password = Password
        self.__Name = Name
        self.__Age = Age
        self.__City = City
        self.__Account_number = Account_number
    
    def createuser(self):
        # INSERT INTO the correct table 'customers'
        temp = db_query( f"INSERT INTO customers VALUES('{self.__Username}', '{self.__Password}', '{self.__Name}', '{self.__Age}', '{self.__City}', '{self.__Account_number}', 0 , 1);")
        mydb.commit()
