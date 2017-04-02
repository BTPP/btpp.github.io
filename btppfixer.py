import glob
fileList = glob.glob("*.html")
for x in fileList:
	newFileName = x+"1"
	outfile = open(newFileName, "w")
	with open(x) as f:
		skip = False
		for line in f:
			if line[:6] == '<style':
				outfile.write("<link href = \"res/styles.css\" rel=\"stylesheet\">")
				skip = True
			if not skip:
				outfile.write(line)
			if line[:7] == '</style':
				outfile.write(line)
				skip = False
	outfile.close()
	f.close()
