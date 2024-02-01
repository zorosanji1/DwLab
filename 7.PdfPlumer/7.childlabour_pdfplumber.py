import pandas as pd
excel_file_path=r"C:\Users\gokul\Desktop\DW Lab\7.PdfPlumer\Child-marriage-database.xlsx"
df=pd.read_excel(excel_file_path)
table_data=df.values
print(table_data)