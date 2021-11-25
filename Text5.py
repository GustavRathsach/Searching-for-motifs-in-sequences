#!/usr/bin/env python3

#[position, penalty, base1, base2, base3]


#ASK FOR PENALTY SCORE CHANGE TO INPUT WHEN DONE!!!!!!!!!!!!!!
maxpenalty=10



#PENALTY PROGRAM HERE:
########################################################################################



#Imported needed packages

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

	#Input control
		#Der er 3 mulig inlinjer
			# - # som er kommentar og har formatet		# xxxxx xxxx xxx
			# - * som er space og har formatet 			*	xx - xx
			# - linje som har formatet 					XXX	xx


	#Making list for the unimportant sequense, and add to overall list
	if line[0] == '*':
		Space = re.search(r'\s+([0-9]+)-([0-9]+)', line)
		AddSpace = [[Position, 'Space', Space.group(1), Space.group(2)]]
		Signal += AddSpace
		Position += 1
		
	#Making list for each position with bases and penalty for this position
	if not line[0] in ['#', '*']:
		Nucleotide = re.search(r'([A-Z]{1,19})\s+([0-9]+)', line)
		Bases = split(Nucleotide.group(1))
		AddNucleotide = [Position, Nucleotide.group(2)]
		AddNucleotide.extend(Bases)
		Signal += [AddNucleotide]
		Position += 1
#print(Signal)

#The output is a list of list with the following formats:
#[position, penalty, base, base, base]
#[position, 'space', min, max]


#END OF PENALTY PROGRAM, start functions
#######################################################################################################

def lead(Motif, MaxPenalty, Pos, sequence, length):
	MotifStart = []
	MotifParts = []
	#for i in range(len(Pos)-1):
	MotifStart+= [Motif[int(Pos[0]):int(Pos[1])]]
	for i in range(len(Pos)-2):
		MotifParts+= [Motif[int(Pos[i+1]):int(Pos[i+2])+1]]
	for i in range(len(MotifParts)):
		if MotifParts[i][-1][1] == 'Space':
			del MotifParts[i][-1]
			#print('found space')
	#print('Start', MotifStart)
	#print('Parts', MotifParts)
	#print(MotifParts[0])
	#print('lenMotif', len(MotifParts))
	CurrentList = start(sequence, MotifStart[0], MaxPenalty, length)	
	#print(CurrentList)
	for i in range(len(MotifParts)):
		CurrentList = space(sequence, MotifParts[i], MaxPenalty, length, CurrentList)
		#print(CurrentList)
	#print(space(sequence, MotifParts[1], MaxPenalty, length, CurrentList))
	return CurrentList





def start(Sequence, MotifStart, MaxPenalty, Length):
	Penalty = 0
	Seq = ''
	FinalSeq = []
	#print('AAAAAA', MotifStart)
	for i in range(len(Sequence)-Length):
		#while Penalty <= MaxPenalty:
			for j in range(len(MotifStart)):
				#print(MotifPart[j][2:])
				if Sequence[i+j] in MotifStart[j][2:]:
					Penalty += 0
					Seq += Sequence[i+j]
					#print(Sequence[i+j])
					#print(MotifPart[j][2:])
					#print('Er til stede')
					#print('a',i,j)		
					#print(' ')
					
				if Sequence[i+j] not in MotifStart[j][2:]:
					Penalty += int(MotifStart[j][1])
					Seq += Sequence[i+j]
					#print(Sequence[i+j])
					#print(MotifPart[j][2:])
					#print('Er ikke til stede')
					#print('b',i,j)
					#print(' ')	
			if Penalty <= MaxPenalty:
				StartPos = i
				FinalSeq += [[Seq, Penalty, i, j, StartPos]]
				Penalty = 0
				Seq = ''
				
			if Penalty > MaxPenalty:
				Penalty = 0
				Seq = ''	
	return FinalSeq
	
def space(Sequence, MotifPart, MaxPenalty, Length, CurrentList):
	Seq = ''
	FinalSeq = []
	minimum = int(MotifPart[0][2])
	maximum = int(MotifPart[0][3])+1
	#print(CurrentList)
	for element in range(len(CurrentList)):
		#print(CurrentList)
		#print('element', element)
		#print(CurrentList[element][2])
		#print(CurrentList[element][3])
		#print('a', CurrentList[element][2]+CurrentList[element][3]+minimum, CurrentList[element][2]+CurrentList[element][3]+maximum)
		#print('min', minimum)
		#print('max', maximum)
		#print('b', len(CurrentList))
		#print(MotifPart)
		#print('c', len(MotifPart))
		#print('d', len(Sequence))
		#print(CurrentList[element])
		for i in range(CurrentList[element][2]+CurrentList[element][3]+minimum,CurrentList[element][2]+maximum):
			#while Penalty <= MaxPenalty:
				Penalty = CurrentList[element][1]
				#if CurrentList[element][2]+CurrentList[element][3]+maximum
				#print(CurrentList[element][2]+CurrentList[element][3]+minimum,CurrentList[element][2]+CurrentList[element][3]+maximum)
					
				for j in range(1,(len(MotifPart))):
					#print('e', i, j, i+j)
					#print(MotifPart[j][2:])
					
					if Sequence[i+j] in MotifPart[j][2:]:
						Penalty += 0
						Seq += Sequence[i+j]
						#print(Sequence[i+j])
						#print(MotifPart[j][2:])
						#print('Er til stede')
						#print('a',i,j)		
						#print(' ')
					#print(MotifPart[j][1])
					if Sequence[i+j] not in MotifPart[j][2:]:
						Penalty += int(MotifPart[j][1])
						Seq += Sequence[i+j]
						#print(Sequence[i+j])
						#print(MotifPart[j][2:])
						#print('Er ikke til stede')
						#print('b',i,j)
						#print(' ')	
				if Penalty <= MaxPenalty:
					if len(CurrentList[element]) < 6:
						FinalSeq += [[Seq, Penalty, i, j, CurrentList[element][4], CurrentList[element][0], i-(CurrentList[element][2]+CurrentList[element][3])]]
						Penalty = 0
						Seq = ''
				
					elif len(CurrentList[element]) >= 6:
						Res = [Seq, Penalty, i, j, CurrentList[element][4]]
						#print(Res)
						for Pos in range(5, len(CurrentList[element])):
							Res += [CurrentList[element][Pos]]
							#print('AAA', Res)
						#FinalSeq += [[Seq, Penalty, i, j, CurrentList[element][4], CurrentList[element][5:], CurrentList[element][0], i-(CurrentList[element][2]+CurrentList[element][3])]]
						FinalSeq += [Res + [CurrentList[element][0], i-(CurrentList[element][2]+CurrentList[element][3])]]
						#print(FinalSeq)
						Penalty = 0
						Seq = ''
						
				if Penalty > MaxPenalty:
					Penalty = 0
					Seq = ''	
	return FinalSeq







#End functions, start execution
#######################################################################################################


length=0   
Motifparts = 1
Spacepos = [0]
for element in Signal:
	if element[1] == 'Space':
		length += int(element[3])-1
		Motifparts += 1
		Spacepos += [element[0]]
length += len(Signal)
Spacepos.append(Signal[-1][0])


#print('length:', length, 'SpacePos:', Spacepos)


outfile = open('Result.txt','w')						#open files, pretty standard
infile = open('motif.fsa','r')

#define variable that holds DNA sequence in a string
sequence = ''

#list for different entries after a space
StartPos = 0


for line in infile:						#read through the file
	
	if line.startswith('>'):			#finds entries
		IDline = line
		line = infile.readline()			#skips to sequence
		sequence = ''
		
		while line.rstrip() != '':		#ensures we are stopping after the sequence
			
			sequence = str(sequence + line.rstrip())		#creates string with the sequence
			line = infile.readline()
		
		#print(IDline)
		#print(sequence)
		Result = lead(Signal, maxpenalty, Spacepos, sequence, length)
		#print(Result)
		#print(len(Result))
		outfile.write(IDline)
		if Result == []:
			outfile.write('There are no match for in motif in this sequense' + '\n' + '\n')
		
		elif Result != []:
			outfile.write('The match(s) of motif in this sequence is/are: ' + '\n')
			for i in range(len(Result)):
				Seq = ''
				StartPos = str(Result[i][4])
				FinalPenalty = str(Result[i][1])
				for j in range(5,len(Result[i])):
					if isinstance(Result[i][j], int):
						Seq += '*' + str(Result[i][j]) + '*'
					else:
						Seq += str(Result[i][j])
				Seq += str(Result[i][0])
				
				outfile.write('The sequence for this match is: ' + Seq  + '\n')
				outfile.write('This match has a starting position at: ' + StartPos + ' and a penalty of ' + FinalPenalty + '\n' + '\n')
		outfile.write('\n')
		
		#outfile.write(Result)
		#print(Result)
				
		
			
		
#Write in outfile
############################