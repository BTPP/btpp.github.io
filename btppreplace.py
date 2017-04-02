import glob
fileList = glob.glob("*.html1")
for x in fileList:
	newFileName = x[:-1]
	outfile = open(newFileName, "w")
	with open(x) as f:
		for line in f:
			outfile.write(line)
	outfile.close()
	f.close()
