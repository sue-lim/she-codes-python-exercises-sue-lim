import csv

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)

        colours = []

# with open("colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader (csv_file)
#     for line in reader: 
#         colours.append (line)

# print(str(colours))


