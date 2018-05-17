import numpy as np
import csv
from pprint import pprint

path = 'C:/Users/hughli/Desktop/test/'
csvfile = open(path + "3sjt110421-csv.csv")
table = csv.reader(csvfile)
nrows = 0
ncols = 0
#table = csvfile.sheets()[0]  
#print(table)  
for index, row in enumerate(table):
    nrows += 1
    if index == 0:
        headings = ','.join(row)
        head = headings.split()
        ncolsori = len(head)
        ncols = int(ncolsori)
        colnum = ncols-5
        print (ncols)
        for k in range(7,colnum):
            print (row[k])  
rowperpiece = (nrows - 3)/5
rpp = round(rowperpiece)
pprint(nrows)
pprint(ncols)
pprint(rpp)

##productid = str(table.details[1][1])
#lotidori = str(table.get_col_row(1, 3))
#dateori = str(table.get_col_row(4, 2))
#lotid = lotidori[1:6]
#date = '20'+str(dateori[6:8]) +'-'+ str(dateori[0:2]) +'-'+str(dateori[3:5])
#pprint(productid)
#pprint(lotid)
#pprint(date)