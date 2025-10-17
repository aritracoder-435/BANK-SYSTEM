# DATABASE MANAGEMENT BANKING SYSTEM
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="hello@12",
    database="BANKING"
)

cursor = mydb.cursor()

def db_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers(
            Username varchar(20) NOT NULL,
            Password varchar(20),
            Name varchar(20) NOT NULL,
            Age int NOT NULL,
            City varchar(20) NOT NULL,
            Account_number INTEGER NOT NULL,
            Balance INTEGER NOT NULL,
            Status boolean NOT NULL )
    ''')
    mydb.commit()

# Ensure table exists when running database.py directly
if __name__ == "__main__":
    createcustomertable()
