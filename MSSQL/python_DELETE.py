import setting

conn = setting.CreateConnection().cursor()

count = conn.execute("""
DELETE Products WHERE ProductID=79
""").rowcount
conn.commit()
print('Rows inserted: ' + str(count))