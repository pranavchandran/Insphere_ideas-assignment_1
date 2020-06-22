inFile = open(filename,'r')
outFile = open('2.csv','w')
listLines = []
for line in inFile:
    for x in inFile:
        if line in x:
            continue 
        else:
            outFile.write(line)
            listLines.append(line)
            break
outFile.close()
inFile.close()