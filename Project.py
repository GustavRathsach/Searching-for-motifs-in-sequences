#!/usr/bin/env python3

#Imported needed packages
import re
import sys

#Asking for file
try:
	Infile = input('Please enter the signal deciption file: ')
except IOError as error:
	print('Can\'t open file, reason:', str(error))

#Reading signal deciption file
SignalFile = open(Infile, 'r')


#Define variables to use
Signal = []
AddNucleotide = []
AddSpace = []
Position = 0

#Split nucleotides at same position
def split(sequence):
	Bases = []
	for base in sequence:
		Bases.append(base)
	return Bases

#Reading each lin in the file
for line in SignalFile:

	#Making list for the unimportant sequense, and add to overall list
	if line[0] == '*':
		Space = re.search(r'\s+([0-9]+)-([0-9]+)', line)
		AddSpace = [[Position, 'Space', Space.group(1), Space.group(2)]]
		Signal += AddSpace
		Position += 1
		
	#Making list for each position with bases and penalty for this position
	if not line[0] in ['#', '*']:
		Nucleotide = re.search(r'([ATCG]{1,3})\s+([0-9]+)', line)
		Bases = split(Nucleotide.group(1))
		if len(Bases) == 1:
			AddNucleotide = [[Position, Nucleotide.group(2), Bases[0]]]
		if len(Bases) == 2:
			AddNucleotide = [[Position, Nucleotide.group(2), Bases[0], Bases[1]]]
		if len(Bases) == 3:
			AddNucleotide = [[Position, Nucleotide.group(2), Bases[0], Bases[1], Bases[2]]]
		Signal += AddNucleotide
		Position += 1
print(Signal)

#The output is a list of list with the following formats:
#[position, penalty, base, base, base]
#[position, 'space', min, max]
