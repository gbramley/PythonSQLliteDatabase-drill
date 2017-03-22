

import sqlite3
rosterValues= (('Jean-Baptiste Zorg','Human',122), ('Korben Dalles','Meat Popsicle', 100),("'Ak''not'",'Mangalore', -5))
with sqlite3.connect('ram.db') as connection:
    c = connection.cursor()
c.execute("DROP TABLE IF EXISTS Roster")
c.execute("CREATE TABLE Roster(Name TEXT,Species TEXT,IQ INT)")
c.executemany("INSERT INTO Roster VALUES(?,?,?)", rosterValues)
c.execute("UPDATE Roster SET Species='Human' WHERE Species='Meat Popsicle'")
c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
row=c.fetchall()
print (row)




