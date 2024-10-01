# lab 1 - CSV
# author: Sylvia Chapman Kent
# read in a CSV file , output the data and calculate the average age

import csv

FILENAME = "data.csv"
DATADIR = "../mywork/"

'''

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter = ",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # header row
            pass # skip header row
        else: # all other rows
            total += int(line[1]) # convert string to integer
        linecount += 1
    print(f"average is {total/(linecount-1)}")  # can't include header row as part of the line count as it'd give the incorrect average if included

'''

# alternative option: read in CSV file as a dictionary object

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter = ",", quoting = csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        print (line)
        count += 1
    print(f"average is {total/(count)}") # no need to put -1 as no header row