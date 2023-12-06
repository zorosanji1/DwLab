import pandas as pd
excel_file=r"C:\Users\gokul\Desktop\DW Lab\5.To_import the excel_data\Child-marriage-database.xlsx"
df=pd.read_excel(excel_file)
data_types=df.dtypes
last_ten_rows=df.tail(10)
new_column=["Nan"]* len(df)
print(data_types)
print(last_ten_rows)
df.insert(5,"Added_Column",new_column)
df.to_excel(excel_file,index=False)
print(df.head())
