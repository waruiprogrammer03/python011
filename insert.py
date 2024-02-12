import sqlite3

conn = sqlite3.connect('afternoon.db')
print("opened database successfuly")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',34, 34000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'MERCY BOKEI',32, 120000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'ALLAN KARANI',27, 85000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'BILL KAMAU',41, 560000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'JANE KARIUKI',23, 345000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()
