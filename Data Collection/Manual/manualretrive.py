import csv

with open ("Data Collection/Manual/manual.csv","r") as rcsv:
    csv_reader=csv.reader(rcsv)
    # print(csv_reader)
    field=next(csv_reader)
    # print(field)
    for line in csv_reader:
        print(line)