#!/usr/bin/python3.6

import csv
import random

with open('database.csv', newline='') as csvfile:
	dt = list(csv.reader(csvfile, delimiter=',', quotechar='|'))


p = [1/len(dt) for i in range(len(dt))]
w = 0.1

while 1:
	choice = random.randrange(10000)/10000
	level = 0
	k=0
	while level < choice:
		level += p[k]
		k += 1
	k -= 1

	res = input("What is the answer for: \n"+str(dt[k][0])+"? (q to stop)\n")
	if res == 'q':
		break
	if res != dt[k][1]:
		print("It was ",str(dt[k][1]),"!")
		p = [(1-w)*x for x in p]
		p[k] = p[k]/(1-w)
		p[k] += w*(1-p[k]) 
	else:
		print("Correct!")
		p[k] -= w*p[k]
		p = [(1+w*p[k]/(1-p[k]))*x for x in p]
	
	print("\nProbability goes to ",str(round(p[k]*10000)/100),"%")
	wait = input("\nContinue?\n")

