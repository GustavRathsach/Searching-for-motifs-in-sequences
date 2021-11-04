#!/usr/bin/env python3

bases='AGNA'
totalscore=0

#random dict i use to check if stuff works, DELETE LATER
def mockscore(sequence):
	#create dict

	scorechart = dict()

	#define dict:

	scorechart = {'A':4, 'T':5, 'G':1, 'C':11,
        'N':15}

	return scorechart[letter]

#for letter in bases:

#	totalscore += mockscore(letter)	
#	print(totalscore)	


	
	
#MAIN PROGRAM STARTS HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
	
	

	
import sys

outfile=open('results.txt','w')						#open files, pretty standard
infile=open('motif.fsa','r')
line=infile.readline()

#define variable that holds DNA sequence in a string
sequence=''

for line in infile:						#read through the file
	
	if line.startswith('>'):			#finds entries
		#print(line)
		line=infile.readline()			#skips to sequence
	
		while line.rstrip() != '':		#ensures we are stopping after the sequence
			#print(line)
			
			sequence=str(sequence + line.rstrip())		#creates string with the sequence
			line=infile.readline()
			
		

		#FUNCTION STARTS HERE
		totalscore=0
		
		for i in range(len(sequence)):
			letter=sequence[i]
			
			tatascore=0
			#totalscore += mockscore(sequence[i])
			for j in range(i,i+8):					#REPLACE WITH LENGHTH BEFORE "#"
				penaltyscore += mockscore(sequence[j])
			
			if penaltyscore > 30:	#REPLACE WITH THE INPUT!!!!!!
				break
			#for j in range(i+8, i+8+SPACE)
			
			
				
				print(sequence[i:i+8])
				print(tatascore)
				tatascore=0
				
		
		#print(sequence)
		#print(totalscore)
		
		
		
		#FUNCTION ENDS HERE
		
		
		
		sequence = '' 									#resets the string to hold next gene

#print(totalscore)
		

infile.close()
outfile.close()




score until #

for i in (startspace , slutspace)
	penalty += sequence[startspace]





