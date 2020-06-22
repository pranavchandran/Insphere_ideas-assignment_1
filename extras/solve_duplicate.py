# solving Duplicate

import fileinput
filename = "worktime_records.csv"

# seen = set() # set for fast O(1) amortized lookup
# for line in fileinput.FileInput(filename, inplace=1):
#     if line in seen: continue # skip duplicate

#     seen.add(line)
#     print(line) # standard output is now redirected to the file

# with open(filename,'r') as in_file, open('2.csv','w') as out_file:
#     seen = set() # set for fast O(1) amortized lookup
#     for line in in_file:
#         if line in seen: continue # skip duplicate

#         seen.add(line)
#         out_file.write(line)

# from more_itertools import unique_everseen,unique_to_each

# inFile = open(filename,'r')

# outFile = open('2.csv','w')

# listLines = []

# for line in inFile:

#     if line in listLines:
#         continue

#     else:
#         outFile.write(line)
#         listLines.append(line)

# outFile.close()

# make by me its working but name is not because all data and time
# is different

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

# import csv

# with open(filename) as f:
#   data = list(csv.reader(f))
#   new_data = [a for i, a in enumerate(data) if a not in data[:i]]
#   with open(filename, 'w') as t:
#      write = csv.writer(t)
#      write.writerows(new_data)

