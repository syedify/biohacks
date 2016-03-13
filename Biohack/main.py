import sys
import os
import time
import xml.etree.ElementTree as ET


def runBlast(cmd1, cmd2):
	os.system(cmd1)
	time.sleep(1)
	os.system(cmd2)

def getcontent(tag,readline):
	tag_length = len(tag) + 2
	content = readline.lstrip()
	return content[tag_length:-1*(tag_length+2)];

def createCSV():
	pass



def main():
	print ("Hello")
	cmd1 = 'makeblastdb -in cold.faa -out coldout -parse_seqids -dbtype prot'
	cmd2 = 'blastp -db coldout -query analysis.fa >analysis.txt'
	#runBlast(cmd1,cmd2)
	#file = open('analysis.txt', 'r')
	#print (file.read())
	#tree = ET.parse('test.xml')
	file = open("ADR15Q3.xml")
	line = file.readline()
	patient_tag = False;
	reaction = False;
	drug_tag = False;

	p_count  = 1
	#csv_string = ""
	reaction_str = ""
	medicial_str = ""
	patient_str = ""

	print ("Patient,Drugs,Event,")
	while line:
		if ("patient>" in line):
			patient_tag = not patient_tag
			if (patient_tag):
				patient_str = str(p_count)
		#		print ("<patient_tag>")
				p_count = p_count + 1

			else:
				csv_string = "{0},{1},{2},".format(patient_str,medicial_str[:-1],reaction_str[:-1])
				#print (csv_string, end="", flush = True)
				print (csv_string)
				reaction_str = ""
				medicial_str = ""
				patient_str = ""
		#		print ("</patient_tag>")

				
		#if ("drug>" in line):
		#	drug_tag = not drug_tag

		#if (patient_tag and ("<reactionmeddrapt>" in line ) and ("Blood glucose increased" in line)):
		#	print (getcontent("reactionmeddrapt",line))
		#	print (line)

		if (patient_tag and ("<reactionmeddrapt>" in line )):
			#reaction_str = "{0},".format(getcontent("reactionmeddrapt", line))
			reaction_str = reaction_str + getcontent("reactionmeddrapt", line) + ";"
			
			#print (reaction_str)
		#	print (line)
			#print (getcontent("reactionmeddrapt",line))

		if (patient_tag and ("<medicinalproduct>" in line )):
			#medicial_str = "{0},".format(getcontent("medicinalproduct", line))
			medicial_str = medicial_str + getcontent("medicinalproduct", line)+ ";"
			#print (medicial_str)
			#print (getcontent("medicinalproduct",line))
		#	print (line)

		line = file.readline()

	file.close()



if __name__ == "__main__":
    sys.exit(int(main() or 0))