import sys
import os
import time
import xml.etree.ElementTree as ET


def runBlast(cmd1, cmd2):
	os.system(cmd1)
	time.sleep(1)
	os.system(cmd2)

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
	patient = False;
	reaction = False;
	drug = False;
	medicinalproduct = False;
	BloodGlucose = 0
	patient_count  = 1

	while line:
		if ("patient>" in line):
			patient = not patient
			if (patient):
				print (patient_count)
				print ("<patient>")
				patient_count = patient_count + 1
			else:
				print ("</patient>")

				
		if ("drug>" in line):
			drug = not drug

		if (patient and ("<reactionmeddrapt>" in line ) and ("Blood glucose increased" in line)):
			print (line)

		if (patient and drug and ("<medicinalproduct>" in line )):
			print (line)

		line = file.readline()

	file.close()



if __name__ == "__main__":
    sys.exit(int(main() or 0))