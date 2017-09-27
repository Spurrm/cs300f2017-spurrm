from collections import Counter
#!/usr/bin/env python

#*******************************
# Mikey Spurr
# CMPSC 300 Fall 2017
# Date: 26 Sept, 2017
# Honor Code
# Purpose: Reading and writing FASTA files using the BioPython libraries
#*************************************

from Bio import SeqIO

myFile_str = raw_input("  Enter File :") #Enter file name to read from
data_str = open(myFile_str)	#opens file
data_str.close()	#close file

#my_file = open('Diabetes.fasta')
listt=[]

#for record in SeqIO.parse(my_file,'fasta'):
for record in SeqIO.parse(myFile_str,'fasta'):
	id = record.id
	seq = record.seq
	print 'File Name: ', myFile_str #prints the entered files name
	print 'Name: ', id	#prints the name of the DNA sequence
	print 'Size: ', len(seq)	#prints the length of the sequence
	print 'Sequence: ', seq		#prints out the whole DNA sequence

	print Counter(seq)			#counts each of the bases in the DNA sequence
	#	print Counter(myFile_str(seq))
	if "tgc" in seq and "cgc" in seq:
		listt.append(record)
		#myFile_str.close()

		outFileName_str = myFile_str + "_out.fasta"	#adds "_out.fasta" to the file name after it is run
		#output_file = open("new_record.fasta", "w")
		outputFile_str = open(outFileName_str,"w")
		
		SeqIO.write(listt, outputFile_str, "fasta")
		outputFile_str.close()
