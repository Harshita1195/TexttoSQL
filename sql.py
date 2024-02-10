import sqlite3

# connect to sqlite
connection=sqlite3.connect("student.db")

# cursor object to inserrt record, create table, retrieve
cursor= connection.cursor()

# create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)
# insert some more records

cursor.execute('''Insert Into STUDENT values('Voilet', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Dolby', 'Data Science', 'B', 100)''')
cursor.execute('''Insert Into STUDENT values('Tim', 'Data Science', 'B', 80)''')
cursor.execute('''Insert Into STUDENT values('Finch', 'DEVOPS', 'A', 70)''')
cursor.execute('''Insert Into STUDENT values('Alaska', 'DEVOPS', 'A', 88)''')

# Display all the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()