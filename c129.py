import csv 
dataset_1 = []
dataset_2 = []

with open ("dwarf_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open ("bright_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

headers1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers1+headers2
planet_data = []

for index,datarow in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open ("final_data.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)