#!/usr/bin/env python3
import re

Infile = input('Please enter the signal deciption file: ')
SignalFile = open(Infile, 'r')

"""
Signal = dict()
for line in SignalFile:
	if line[0] == '*':
		Signal['space'] = line[2:-1].split(sep='-')
	if not line[0]in ['#', '*']:
		Signal[line[0]] = line[2:-1]
print(Signal)

count = 0	
count2 = 0
Nucleotide = dict()
Penalty = dict()
for line in SignalFile:
	if line[0] == '*':
		MinSpace = re.search(r'\s+([0-9]+)-[0-9]+', line)
		Nucleotide[count] = MinSpace.group(1)
		count += 1
	if not line[0] in ['#', '*']:
		Nucleotide[count] = line[0]
		count += 1
	if line[0] == '*':
		MaxSpace = re.search(r'\s+[0-9]+-([0-9]+)', line)
		Penalty[count2] = MaxSpace.group(1)
		count2 += 1
	if not line[0] in ['#', '*']:
		Penalty[count2] = line[2]
		count2 += 1
		
print(Nucleotide)
print(Penalty)


"""



