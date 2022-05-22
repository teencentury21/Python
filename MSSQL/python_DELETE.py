import setting

conn = setting.CreateConnection().cursor()

count = conn.execute("""
DELETE Products WHERE ProductID=82
""").rowcount
conn.commit()
conn.close()
print('Rows inserted: ' + str(count))