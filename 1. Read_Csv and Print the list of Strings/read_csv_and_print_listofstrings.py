import csv
with open(r"C:\Users\gokul\Desktop\DW Lab\1. Read_Csv and Print the list of Strings\departments.csv",
           newline="") as csvfile:
              data=csv.reader(csvfile,delimiter=" ",quotechar="|")
              for row in data:
                            for value in row:
                                          print(value)
