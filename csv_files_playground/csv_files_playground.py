import csv

# readin csv from a file 
# import the csv file with csv reader, loop through each line and print it / add into populaton list
with open ("2016_pilbara.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
        
        population = []
        
with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader (csv_file)
    for line in reader:
        # print these in a line 
        population.append (line)

print(population)
print()

# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")
#     # numbers above are column numbers, read and print these into string 
            
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     # write these with commas inbetween 

#     for age_group in population: 
#         csv_writer.writerow([age_group[0], age_group[1]])
#         #  The writerow method writes a row of data into the specified file.