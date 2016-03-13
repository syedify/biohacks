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
	tree = ET.parse('test.xml')
	root = tree.getroot()
	for child in root:
		print (child.tag, child.attrib)
	



if __name__ == "__main__":
    sys.exit(int(main() or 0))