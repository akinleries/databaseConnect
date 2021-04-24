#Connect to mysql database using python and retrieve some data

#import the needed packages

import mysql.connector
from mysql.connector import Error

#define the connector function

def Connect_fetch():
    '''function to connect and fetch rows in a database'''

    #create a variable for the connect object

    conn = None

    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'lasisi')
        print('Connecting to database server')
        if conn.is_connected:
            print('connected to database server')

         #select Query
        sql_select_query = "select * from Human"
        cursor = conn.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print('total number of rows in Human: ',  cursor.rowcount)

       #Display the output data
        print("\nPrinting each rows in Human")
        for row in records:
            print("HumanId: ", row[0])
            print("name", row[1])
            print("color", row[2])
            print("Sex", row[3])
            print("BloodGroup", row[4], '\n')

    except Error as e:
              print('not connecting due to : ', e)

    finally:
        if conn is not None and conn.is_connected():
              conn.close()
              print('database shutdown')


Connect_fetch()
