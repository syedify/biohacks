import sys
import os
import time
import xml.etree.ElementTree as ET

#THIS IS JUST A BAKUP MAIN FUNCTION IS MAIN.PY
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

	while line:
		if ("patient>" in line):
			patient = not patient

		#if(line.find("</patient>")):
		#	patient = False

		if ("drug>" in line):
			drug = not drug

	#	if (line.find("</drug>")):
	#		drug = False

		if (patient and drug and ("<medicinalproduct>" in line )):
			print (line)

		line = file.readline()

	file.close()
	'''
	root = tree.getroot()
	for child in root:

for patient in root.findall ('patient')
		print (child.tag, child.attrib)
'''






if __name__ == "__main__":
    sys.exit(int(main() or 0))
