import mysql.connector

z = input("Host you want to connect to: ")
x = input("Database you want to enter: ")
y = input("Username: ")
q = input("Password: ")

def prs():
    if z == "cigosbaran":
        print("xxxx")
        database = mysql.connector.connect(
        host="localhost",
        user="xcredentialsx",
        password="xxxxx",
        database="credentials"
        )
        mycursor.execute("CREATE TABLE userandpass (name VARCHAR(255), pass VARCHAR(255))")
        
    else:
        pass
prs()

try:
    print("Database exists, logging in.")
    database = mysql.connector.connect(
        host=z,
        user=y,
        password=q,
        database=x
        )
#except(SyntaxWarning): Except no connection
except(SyntaxError):#change to actual mysql database doesnt; Exception to no database found error
    print("Database has not been found, creating one for you. Please wait")
    databaser = mysql.connector.connect(
        host=z,
        user=y,
        password=q,
        )
    mycursor = databaser.cursor()
    mycursor.execute("CREATE DATABASE " + x)
    print("Logging in!")
    database = mysql.connector.connect(
        host=z,
        user=y,
        password=q,
        database=x
        )

    #qestt()
#def qestt():
   # qest = input("Do you wanna create table? y/n: ")
   # if qest == "y" or "yes":
    #   cicka = input("Name of the table; ")
     #   mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

def lmao():
    name = input("Name: ")
    passq = input("Do you want us to create your password ? y/n: ")
    if passq == "y" or "yes":
        #Generate password
    password = input("Enter your password: ")