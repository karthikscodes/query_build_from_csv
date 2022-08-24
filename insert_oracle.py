### for oracle

import csv

rows = []
with open("C:/Users/acer/Downloads/file.csv", 'r') as file:
          csvreader = csv.reader(file)
          header = next(csvreader)          
          for row in csvreader:
            cmd="Insert into table values "
            cmd=cmd+"( '"
            for j in row:
              cmd=cmd+str(j)+"','"
            cmd=cmd[0:-2]
            cmd=cmd+");"
            print(cmd)
            cmd=cmd[0:-2]+"),"
