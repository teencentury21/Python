import pandas as pd
 
 
grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
 
df = pd.DataFrame(grades)
 
print("使用字典來建立df：")
print(df)
 
print("=====================")
 
grades = [
    ["Mike", 80, 63],
    ["Sherry", 75, 90],
    ["Cindy", 93, 85],
    ["John", 86, 70]
]
 
new_df = pd.DataFrame(grades)
 
print("使用陣列來建立df：")
print(new_df)