from typing import Tuple

import mysql.connector

#Connect to Database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "CST2355",
    password = "CST2355Database",
    database = "musa"
)
#Make a cursor object for mySQL
mycursor = mydb.cursor()

#Open .txt File

# *Need to create an input to ask user to type in a .txt filename*
with open('config.txt') as f:
    #for loop to iterate through lines (iterates for as many lines there are)
    for line in f:
        #split lines into a list so data can be separated and stored into variables
        list = line.split(",")

        #data is stored into variables based on index of the list
        asset = list[0]
        new = list[1]
        thing = list[2]
        do = list[3]
        what = list[4]

        #MySQL insert statement
        sql = "INSERT INTO testing (firstname, lastname, city, province, phone) VALUES(%s, %s, %s, %s, %s)"
        val = (asset, new, thing, do, what)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")

