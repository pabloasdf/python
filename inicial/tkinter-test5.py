import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    sql_select_Query = "select * from Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

When you execute the above example, you should get the following output.

Total number of rows in Laptop is:  7
Printing each laptop record

Id =  1
Name =  Lenovo ThinkPad P71
Price  =  6459.0
Purchase date  =  2019-08-14 

Id =  2
Name =  Area 51M
Price  =  6999.0
Purchase date  =  2019-04-14 

Id =  3
Name =  MacBook Pro
Price  =  2499.0
Purchase date  =  2019-06-20 

Id =  4
Name =  HP Pavilion Power
Price  =  1999.0
Purchase date  =  2019-01-11 

Id =  5
Name =  MSI WS75 9TL-496
Price  =  5799.0
Purchase date  =  2019-02-27 

Id =  6
Name =  Microsoft Surface
Price  =  2330.0
Purchase date  =  2019-07-23 

Id =  7
Name =  Acer Predator Triton
Price  =  2435.0
Purchase date  =  2019-08-15 

MySQL connection is closed




