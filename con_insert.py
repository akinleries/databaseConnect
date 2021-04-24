#Connect to mysql database using python and retrieve some data

#import the needed packages

import mysql.connector
from mysql.connector import Error

#define the connector function

def Connect_insert():
    '''function to connect and fetch rows in a database'''

    #create a variable for the connect object

    conn = None

    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'lasisi')
        print('Connecting to database server')
        if conn.is_connected:
           print('connected to database server')
           db_cursor = conn.cursor()

           #create a variable to contain the sql query to be executed
           sql = "insert into Human (HumanId, name, color, Gender, BloodGroup) Values (%s, %s, %s, %s, %s)"

           #create a list variable to contain all the values we want to insert into the table

           val = []
            #    ('1013', 'Hannah', 'white', 'female', 'B-')
            #    ('1014', 'micheal', 'brown', 'male', 'O-')
            #    ('1015', 'sandy', 'Black', 'female', 'B-')

           for countUserInput in range(3):
                HumanId = input("your id number  : ")
                name = input("enter your name pls  : ")
                color = input("your color  : ")
                Gender = input("enter your gender : ")
                BloodGroup = input( "enter your blood Group  : ")
                val.append((HumanId, name, color, Gender, BloodGroup))
           #execute the query using the execute many function
           db_cursor.executemany(sql, val)

           #commit to the database
           conn.commit()

           #print a success message
           print(db_cursor.rowcount, "row was inserted")

           #close the cursor
           db_cursor.close

    except Error as e:
        print('connection failed due to the following', e)
    finally:
        if conn is not None and conn.is_connected:
           conn.close
           print('Disconected from the database')


Connect_insert()

