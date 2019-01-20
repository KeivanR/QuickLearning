#!/usr/bin/python3.6

import csv
with open('database.csv', newline='') as csvfile:
	table = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in table:
		print(', '.join(row))


print(table)
