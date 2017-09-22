import csv
import numpy as np
import pickle

with open('signnames.csv', 'rb') as csvfile:
	signreader = csv.reader(csvfile)
	for row in signreader:
		print((row[0]))
		
print(signreader)
