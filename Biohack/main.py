import sys

def getcontent(tag,readline):
	tag_length = len(tag) + 2
	content = readline.lstrip()
	return content[tag_length:-1*(tag_length+2)];



def main():
	
	#file_name = "ADR15Q3.xml"
	file_name = str(sys.argv[1])

	file = open(file_name)
	line = file.readline()

	patient_tag = False;
	reaction = False;
	drug_tag = False;

	p_count  = 1
	reaction_str = ""
	medicial_str = ""
	patient_str = ""

	print ("Patient,Drugs,Event,")
	while line:
		if ("patient>" in line):
			patient_tag = not patient_tag
			if (patient_tag):
				patient_str = str(p_count)
				p_count = p_count + 1

			else:
				csv_string = "{0},{1},{2},".format(patient_str,medicial_str[:-1],reaction_str[:-1])
				print (csv_string)
				reaction_str = ""
				medicial_str = ""
				patient_str = ""

		if (patient_tag and ("<reactionmeddrapt>" in line )):
			reaction_str = reaction_str + getcontent("reactionmeddrapt", line) + ";"


		if (patient_tag and ("<medicinalproduct>" in line )):
			medicial_str = medicial_str + getcontent("medicinalproduct", line)+ ";"

		line = file.readline()

	file.close()



if __name__ == "__main__":
    sys.exit(int(main() or 0))