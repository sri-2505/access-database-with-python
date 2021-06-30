from tabulate import tabulate
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505"
)

def NewDatabase():
    Dname = input("Enter Your Database Name:")
    mycursor = mydb.cursor()
    sql = "CREATE DATABASE " + Dname
    mycursor.execute(sql)    
    print('Database Created')
    ShowDatabase()
    TableOption(Dname)

def ShowDatabase():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    result = mycursor.fetchall()
    print(tabulate(result,headers=["DATABASES"]))

def SelectDatabase():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    result = mycursor.fetchall()
    print(tabulate(result,headers=["DATABASES"]))

    Dname = input('Enter the database name: ')
    sql = "use " + Dname
    mycursor.execute(sql)
    print('Database Successfully Connected')
    TableOption(Dname)

def DeleteDatabase():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    result = mycursor.fetchall()
    print(tabulate(result,headers=["DATABASES"]))

    Dname = input("Enter the Database Name:")
    sql = "DROP DATABASE " + Dname
    mycursor.execute(sql)    
    print('Database deleted')
    ShowDatabase()

def ShowTables(Dname):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FREDLY2505",
        database=Dname
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    res = mycursor.fetchall()
    print(tabulate(res,headers=["TABLES"]))
    TableOption(Dname)
    

def CreateTable(Dname):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FREDLY2505",
        database=Dname
    )
    Tname = input("Enter the table name: ")
    i = 1
    j = int(input("Enter the No.of column: "))
    column = []
    while i <= j:
        index = i - 1
        i = i + 1
        val = input("enter the column name: ")
        val2 = input("Enter the type: ")
        if i == 2:
            mycursor = mydb.cursor()
            sql="CREATE TABLE " + Tname +" ( " + val + " " + val2 + ")"
            mycursor.execute(sql)
        elif i>2:
            mycursor = mydb.cursor()
            sql="ALTER TABLE " + Tname + " ADD " + val + " " + val2
            mycursor.execute(sql)
        column.insert(index,val)
    i = 0
    j = len(column)
    names = ""
    while i<j:
        if i == 0:
            names = names + column[i]
        else:
            names = names +","+ column[i]
        i = i + 1
    print("Table Creater Successfully")
    RecordOptions(Dname, Tname, column, names)

def SelectTable(Dname):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FREDLY2505",
        database=Dname
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    result = mycursor.fetchall()
    print(tabulate(result,headers=["TABLES"]))
    Tname = input('Enter the table name: ')

    sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = " + "'" + Dname + "'" + " AND TABLE_NAME = " + "'" + Tname + "'"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    column = []
    for x in res:
        column.append(x[0]) 
    
    sql = "SELECT * FROM " + Tname
    mycursor.execute(sql)
    result = mycursor.fetchall() 
    print(tabulate(result,headers=column))

    i = 0
    j = len(column)
    names = ""
    while i<j:
        if i == 0:
            names = " ,".join(column)
        i = i + 1
    print('Table Selected Connected')
    RecordOptions(Dname, Tname, column, names)

def InsertData(Dname, Tname, column, names):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FREDLY2505",
        database=Dname
    )
    k = 0
    j = len(column)
    val2 =" "
    while k<j:
        val = "Enter the value for " + column[k] + ": "
        if k == 0:
            val2 = val2 + "'" + input(val) + "'"
        else: 
            val2 = val2 + "," + "'" + input(val) + "'"       
        k = k + 1
        sql = "INSERT INTO " + Tname + "(" + names +") values (" + val2 + ")"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted., ID:", mycursor.lastrowid)
    RecordOptions(Dname, Tname, column, names)

def DeleteData(Dname, Tname, column, names):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FREDLY2505",
            database=Dname
        )
    mycursor = mydb.cursor()
    print(names)
    col = input("Enter the col name to select record: ")
    sql = "SELECT * FROM " + Tname
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(tabulate(result))

    row = input("Enter the data which you want to delete : ")
    sym = input(" Select the symbol to compare the data '<=','>=','<', '>', '=' : ")

    sql = "DELETE FROM " + Tname + " WHERE " + col + " " + sym + " " + row
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    RecordOptions(Dname,Tname,column,names)

def UpdateData(Dname, Tname, column, names):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FREDLY2505",
        database=Dname
    )
    Tname = 'one'
    mycursor = mydb.cursor()

    print(names)
    col = input("Enter the column name which is to update: ")
    sql = "SELECT * FROM " + Tname
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(tabulate(result))

    val = input("Enter the new data: ")
    print(names)
    col2 = input("Enter the column name where you have a condition: ")
    val2 = input("conditioned value: ")
    sym = input("Enter the symbol to search data '<=','>=',<', '>', '=' : ")
    sql = "UPDATE " + Tname + " SET " + col + " = " + "'" + val + "'" + " WHERE " + col2 + " " + sym + " " + val2
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    RecordOptions(Dname,Tname,column,names)

def ShowDatas(Dname, Tname, column, names):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FREDLY2505",
        database=Dname
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM " + Tname
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(tabulate(result,headers=column))
    RecordOptions(Dname,Tname,column,names)


def RecordOptions(Dname, Tname, column, names):
    print("""
        1. Insert Data
        2. Delete Data
        3. Update Data
        4. Show datas
        5. Back
        6. Exit
        """)
    choice = int(input("Enter Your Option:"))
    if choice == 1:
        InsertData(Dname, Tname, column, names)
    elif choice ==2:
        DeleteData(Dname, Tname, column, names)
    elif choice ==3:
        UpdateData(Dname, Tname, column, names)
    elif choice == 4:
        ShowDatas(Dname, Tname, column, names)
    elif choice == 5:
        TableOption(Dname)
    elif choice == 6:
        exit()
    else:
        print("Please Enter The Value Option")

def TableOption(Dname):
    print("""
        1. Create Table
        2. Show Tables
        3. Selete Table
        4. Back
    """)
    choice = int(input("Enter Your Option:"))
    if choice == 1:
        CreateTable(Dname)
    elif choice ==2:
        ShowTables(Dname)
    elif choice ==3:
        SelectTable(Dname)
    elif choice == 4:
        entry()
    else:
        print("Please Enter The Value Option")

def entry():
    print("""
        1. Create Database
        2. Show Database
        3. Selete Database
        4. Delete Databse
        5. Exit
    """)
    choice = int(input("Enter Your Option:"))
    if choice == 1:
        NewDatabase()
    elif choice ==2:
        ShowDatabase()
    elif choice ==3:
        SelectDatabase()
    elif choice == 4:
        DeleteDatabase()
    elif choice == 5:
        exit()
    else:
        print("Please Enter The Value Option")

if __name__ == '__main__':
    while True:
        entry()
