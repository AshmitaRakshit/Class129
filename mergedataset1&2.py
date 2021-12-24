#merge dataset_1.csv & dataset_2.csv
#open both the files in readmode
#copy the contents in two seperate lists
#find headers1, planet data1 from dataset1
#find headers2 planet data2 from dataset2
#merge the headers 
#merge the planet data
#save the merged data in a new file(mergedataset1&2.csv)

import csv

dataset_1 = []
dataset_2 = []

with open("C:/WhiteHatJr/Class129/dataset_1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("C:/WhiteHatJr/Class129/data2sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("C:/WhiteHatJr/Class129/mergedataset1&2.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
