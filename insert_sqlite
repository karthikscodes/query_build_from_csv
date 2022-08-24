#### for sqlite

import csv

rows = []
with open("C:/Users/acer/Downloads/file.csv", 'r') as file:
          csvreader = csv.reader(file)
          header = next(csvreader)
          cmd="Insert into table values "
          for row in csvreader:
            cmd=cmd+"( '"
            for j in row:
              cmd=cmd+str(j)+"','"
              #print(cmd)
            cmd=cmd[0:-2]+"),"
print(cmd)
