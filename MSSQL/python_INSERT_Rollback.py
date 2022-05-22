import setting

conn = setting.CreateConnection().cursor()

conn.execute("BEGIN TRANSACTION")  
count = conn.execute("""
INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, 
UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
VALUES (?,?,?,?,?,?,?,?,?)""",
'Tofu XXL','6','7','40 - 100 g pkgs.','43.25','10','0','0','0').rowcount
print('Rows inserted: ' + str(count))

conn.rollback()  
conn.close()