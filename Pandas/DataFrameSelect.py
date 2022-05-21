import pandas as pd
 
 
grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
 
df = pd.DataFrame(grades)
df.columns = ["student_name", "math_score", "chinese_score"]  #自訂欄位名稱

print("原來的df")
print(df)
 
print("====head=============================")
 
new_df = df.head(2)
print("取得最前面的兩筆資料")
print(new_df)

print("====tail=============================")
 
new_df = df.tail(3)
print("取得最後面的三筆資料")
print(new_df)