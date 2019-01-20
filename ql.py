#!/usr/bin/python3.6

from ODSReader import ODSReader

doc = ODSReader(u'database.ods', clonespannedcolumns=True)
table = doc.getSheet(u'Sheet1')
for i in range(len(table)):
    for j in range(len(table[i])):
        print (table[i][j])


print(table)
