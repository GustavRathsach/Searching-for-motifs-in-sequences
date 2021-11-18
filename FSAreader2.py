#!/usr/bin/env python3

#[position, penalty, base1, base2, base3]


#ASK FOR PENALTY SCORE CHANGE TO INPUT WHEN DONE!!!!!!!!!!!!!!
maxpenalty=15



#PENALTY PROGRAM HERE:
########################################################################################



#Imported needed packages
import re
import sys

#Asking for file
try:
	#Infile = input('Please enter the signal deciption file: ')
	SignalFile = open('Penalty.txt','r')
except IOError as error:
	print('Can\'t open file, reason:', str(error))

#Reading signal deciption file
#SignalFile = open(Infile, 'r')


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



#END OF PENALTY PROGRAM
#######################################################################################################



#length of signalfile and sequence
length=0
lines=0
for element in Signal:
	lines += 1
	if element[1] == 'Space':
		length += int(element[3])
length += len(Signal)
length += -1
print(len(Signal))
#print(lines)
	
	
#MAIN PROGRAM STARTS HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
	
#print(Signal[2][1])

	


outfile=open('results.txt','w')						#open files, pretty standard
infile=open('motif.fsa','r')
line=infile.readline()

#define variable that holds DNA sequence in a string
sequence=''
sequencenr = 1

#list for different entries after a space
Slist = []
counter=0

for line in infile:						#read through the file
	
	if line.startswith('>'):			#finds entries
		#print(line)
		line=infile.readline()			#skips to sequence
	
		while line.rstrip() != '':		#ensures we are stopping after the sequence
			#print(line)
			
			sequence=str(sequence + line.rstrip())		#creates string with the sequence
			line=infile.readline()
			
		

		
		
		
		
		
		#FUNCTION STARTS HERE
		
		#print(sequence)
		
		#i is a variable for the starting position of our reading frame
		for i in range(len(sequence)-length-1):
		
			#[position, penalty, base1, base2, base3]
			
			penaltyscore=0
			
			#j is a variable for position in the a reading entry
			for j in range(length-1):			#Lines in the amount of lines in the signal file
				#print(sequence[i+j])
				#print(Signal[j][2])
				try:
					#print(sequence[i+j])
					#print(Signal[j][2])
					#print(i)
					if Signal[j][1] == 'Space':
						i += int(Signal[j][2])
						j+=1
						break
					elif sequence[i+j] != Signal[j][2] or sequence[i+j] != Signal[j][3]:
						penaltyscore += int(Signal[j][1])
						
					
					#print(j)
				except IndexError as error:
					if sequence[i+j] != Signal[j][2]:
						penaltyscore += int(Signal[j][1])
						
						#print(j)
			totalpen=penaltyscore
			penaltyscore=0
			
			if totalpen < maxpenalty:			
			###############################################   SAME THING AGAIN, BUT AFTER THE BREAK			
				for j2 in range(int(Signal[j-1][3])-int(Signal[j-1][2])):
				
				#J2 is the range after space, it varies with space interval
			
					for h in range(j,len(Signal)-1):						#h is the sequence positions after the first break. It goes from after the space and until the next space or the end of the signal file
						try:
					#print(sequence[i+j])
					#print(Signal[j][2])
					#print(i)
							
							if Signal[h][1] == 'Space':	

							#the positions are now described by 2 variables because the locations can vary 
							#i gets bigger because the space is added, i counts the position in the sequence
								i += int(Signal[h][2])
								h+=1
								break
							elif sequence[i+h+j2] != Signal[h][2] or sequence[i+h+j2] != Signal[h][3]:
								penaltyscore += int(Signal[h][1])
						
					
						#print(j)
						except IndexError as error:
							
							if sequence[i+h+j2] != Signal[h][2]:
								penaltyscore += int(Signal[h][1])
						
						
							
					#the different starts after the space gets put into a list and sorted and the best value gets extracted
						Slist.append([])
						Slist[counter].append(penaltyscore+totalpen)
						Slist[counter].append(h)
						
						counter+=1
						penaltyscore=0
					sortedSlist=sorted(Slist)
					#print(Slist)
					Slist=[]
					counter=0
					if sortedSlist[0][0] < maxpenalty:
						print(sortedSlist[0], i, sequencenr)    #SORTEDLIST = [PENALTY, WHICH BASE IS COUNTED]
			
			
			
			
			
			#if penaltyscore < 10:	
				#print('Match at sequence number ' , sequencenr, 'at base ',i, 'with a score of: ' ,penaltyscore)
				
		
		#print(sequence)
		#print(totalscore)
		
		
		
		#FUNCTION ENDS HERE
		
		
		
		sequence = '' 		#resets the string to hold next gene
		sequencenr += 1

#print(totalscore)
		

infile.close()
outfile.close()






#for i in (startspace , slutspace)
#	penalty += sequence[startspace]





