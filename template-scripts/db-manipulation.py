# DATABASE MANIPULATION
import os
import sqlite3

# Removes database if exists
os.remove('banco_de_dados.db') if os.path.exists('banco_de_dados.db') else None

# Connects to existing DB, or creates one if it doesn't exist
con = sqlite3.connect('banco_de_dados.db')

# Creates a cursor. Allows going through the database
cur = con.cursor()

# Creates SQL instruction (CREATE)
sql_create = 'CREATE TABLE Tabela ( '\
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '\
    'atributo1 VARCHAR(100), '\
    'atributo2 VARCHAR(100)) '\
# Executes instruction
cur.execute(sql_create)

# Creates instruction (INSERT)
# '?' character is a placeholder for parameters
sql_insert = 'INSERT INTO Tabela VALUES (?,?,?)'
recset = [(1, 'A1', 'B1'),
          (2, 'A2', 'B2'),
          (3, 'A3', 'B3')]
#Executes instruction
for record in recset:
    cur.execute(sql_insert, record)

# Creates instruction (INSERT alternative)
atr1 = 'A4'
atr2 = 'B4'
sql_insert = f'INSERT INTO Tabela (atributo1, atributo2) VALUES ("{atr1}", "{atr2}")'
#Executes instruction
cur.execute(sql_insert)

# Saves transaction when altering the table, like the two commands above
con.commit()

# SELECT
sql_select = 'SELECT * FROM Tabela'
# executes command, selecting wanted data
cur.execute(sql_select)
# fechets the selected data and creates an object
# can think of it as a commit for reading data commands
data = cur.fetchall()
for line in data:
    print('ID: %d, Atributo 1: %s, Atributo 2: %s' % line)

# After workign with a DB, close it!
cur.close()
con.close()

##############################################################################
# It's pretty much the same for MySQL. Expect for, when connecting, you need
# to infor access credentials.

#import mysql.connector
#
#con = mysql.connector.connect(
#    host='localhost',
#    user='root',
#    password='489562',
#    database='database')
