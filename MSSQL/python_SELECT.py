import setting

conn = setting.CreateConnection().cursor()

#Sample select query
conn.execute("SELECT @@version;") 
row = conn.fetchone() 
while row: 
    print(row[0])
    row = conn.fetchone()

#Sample select from table query
conn.execute("SELECT * FROM Northwind..Employees") 
row = conn.fetchone() 
while row: 
    print(row[2]+' '+row[1])
    row = conn.fetchone()