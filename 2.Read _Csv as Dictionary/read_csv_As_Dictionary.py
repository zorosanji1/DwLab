import csv
filename=r"C:\Users\gokul\Desktop\DW Lab\2.Read _Csv as Dictionary\departments.csv"
with open(filename,"r") as data:
              dictfile=csv.DictReader(data)
              for row in dictfile:
                        print(dict(row))
