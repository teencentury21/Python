import setting

conn = setting.CreateConnection().cursor()

count = conn.execute("""
UPDATE Products SET ProductName='Tofu XXXL' WHERE ProductID=79
""").rowcount
conn.commit()
conn.close()
print('Rows inserted: ' + str(count))