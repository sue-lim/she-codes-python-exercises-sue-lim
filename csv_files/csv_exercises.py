# print("########## QUESTION 1 ##########")
# import csv
# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)
# colours = []

# with open("colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)
#     print(colours)
#     print()

# for col_type in colours:
#     print(f"{col_type[1]} {col_type[2]} {col_type[4]}")
    
# print("########## QUESTION 2 ##########")

# import csv
# with open("colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)
# colours = []

# with open("colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)
#     print(colours)
#     print()

# for col_type in colours:
#     # print(f"{col_type[1]} {col_type[2]} {col_type[4]}")
#     print(f"{col_type[2]}, Hex: {col_type[1]}, RGB: {col_type[0]}")
    
    
print("########## QUESTION 3 ##########")

import csv
import collections
with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
colours = []

with open("colours_20.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)
    # print(colours)
#     # print()
# # for line in reader:
 
# for col_type in colours:
#     print(f"{col_type[4]}, Hex: {col_type[2]}, RGB: {col_type[1]}")_
    

with open("colour_20_name.csv", mode="w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    for col_type in colours:
        csv_writer.writerow(col_type)
    
# # #     for col_type in colours:
        
# # #     csv_writer.writerow([col_type[4]])
# with open("colours_20.csv") as csv_file:
#     l = csv.reader(csv_file)
    print(count("yellow"))