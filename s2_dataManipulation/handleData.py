import pandas as pd
import numpy as np

# 1. Data frames and series
series = pd.Series([1,2,3,4,5], index=["a","b","c","d","e"])
print(series)

data = {
    "Name" : ["Phuc1","Phuc2", "Phuc3", "Phuc4", "Phuc5"],
    "Age" : [20,21,22,23,24],
    "City" : ["HCM", "HN", "SG", "JP", "US"]
}
df = pd.DataFrame(data)
print(df)

# 2. Data cleaning and preparation
# 2.1 with Null values
data = {
    "Name" : ["Phuc1","Phuc2", "Phuc3", "Phuc4", "Phuc5"],
    "Age" : [20,np.nan,22,23,np.nan],
    "City" : ["HCM", "HN", np.nan, "JP", "US"]
}
df = pd.DataFrame(data)
print("df with null values:\n", df)
df_fillna = df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'})
print("df with null values filled:\n", df_fillna)

# 2.2 with duplicate values
data = {
    "Name" : ["Phuc1","Phuc2", "Phuc3", "Phuc4", "Phuc1"],
    "Age" : [20,21,22,23,20],
    "City" : ["HCM", "HN", "SG", "JP", "HCM"]
}
df = pd.DataFrame(data)
print("df with duplicate values:\n", df)
df_drop_duplicates = df.drop_duplicates()
print("df with duplicate values dropped:\n", df_drop_duplicates)

# 3. Handling missing data
data = {
    "Name" : ["Phuc1","Phuc2", "Phuc3", "Phuc4", "Phuc1"],
    "Age" : [20,21,np.nan,23,20],
    "City" : ["HCM", "HN", "SG", "JP", np.nan]
}
df = pd.DataFrame(data)
print("df with missing values:\n", df)

missing_values = df.isnull()
print("missing values:\n", missing_values)

df_dropna = df.dropna()
print("df with missing values dropped:\n", df_dropna)

# 4. Merging and joining data
df3 = pd.DataFrame({
    'ID': [1,2,3,4,5],
    'Name': ['Phuc1','Phuc2','Phuc3','Phuc4','Phuc5']
})
df4 = pd.DataFrame({
    'ID': [1,2,3,4,5],
    'Age': [20,21,22,23,24]
})
df_merge = pd.merge(df3, df4, on='ID')
print("df merged:\n", df_merge)

df3 = pd.DataFrame({
    'ID': [1,2,3,4,5],
    'Name': ['Phuc1','Phuc2','Phuc3','Phuc4','Phuc5']
})
df4 = pd.DataFrame({
    'studentID': [1,2,3,4,5],
    'Age': [20,21,22,23,2]
})
df_join = pd.merge(df3, df4, left_on='ID', right_on='studentID')
print("df joined:\n", df_join)
# 5. Sorting and filtering data

# 6. Grouping and aggregation

