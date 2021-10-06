# TextFiletoMySQL


*View in raw format*


Basic Python automation script that opens a .txt file and inserts the data into a MySQL table

I decided to create this script because my current work position as an IT Support Specialist requires me to insert data into a database. Initially, I like to format the data into a .txt file within notepad as: 


            User: John Doe                                                                User, UserID, UserEmail
            UserID: 12356                                   or                           John Doe, 12356, john.doe@domain.com
            UserEmail: john.doe@domain.com                                               Jane Doe, 56789, jane.doe@domain.com 
            
            
            
My goal is to modify this script to ignore the header/text before the semi-colon, so that they can indicate what the information is within the text-file, but not be inserted into the database.

I also plan on modifying this scrit to accept user input - database name, db user, db password, hostname (or to find an easier way for it to connect to the DB so it doesn't need to keep being re-entered. My other plan is to prompt the user to type in the .txt file name and to deal with typo errors. 
Script imports MySQL connector and creates an object containing hostname, password, database name, and the user name, to create or establish a connection to MySQL
Uses a cursor object to allow scripts to be executed into MySQL from python

*Will Add a variable that receives input from user - prompts them to enter .txt name file & handles errors (typos, etc.)*

Use with statement to open file - makes code cleaner then: file = open('file.txt', 'r') 
For loop is used to iterate through the lines, and to split each line into a list so that the data can be gathered by the index, making it easy to insert into the database via the insert query statement. 


  Ex: list = line.split(',') 
      data1 = list[0]
      data2 = list[2]



The data variable tied to the list index value, is placed into the insert query, and when run, it is inserted into MySQL table, and it is printed ("1 record inserted") depending on how many lines there are (since for loop iterates that many times)

*Error that is received in the console - 'data1 = list[1] is out of range' - values still are inserted and '1 record inserted' is printed

Feel free to contact me with any suggestions or ideas you come up with to improve or add to the script!


              Ethan.garr2000@gmail.com  
              garr0118@algonquinlive.com
              
              
Thank you!
      
      
 
