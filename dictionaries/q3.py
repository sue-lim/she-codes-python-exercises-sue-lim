# https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
# scroll to 68

# names = [
#     "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
#     "Joy", "Katie", "Maddie", "Tash", "Nic",
#     "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
#     "Viv", "Anna", "Catherine", "Catherine", "Debby",
#     "Gab", "Megan", "Michelle", "Nic", "Roxy",
#     "Samara", "Sasha", "Sophie", "Teagen", "Viv"
# ]

# names_dictionary = {x:names.count(x) for x in names}
# creating a dictionary keys with the above lists and counting the items

# for key, value in names_dictionary.items():
# applying the relevant count of numbers to the dictionary as a value 
    # print (key, value)
# printing the value & the keys 

    
names = [
    "Miranda", "Sophie", "Emily", "Taylor", "Anne",
    "Djuarli", "Anika", "Rosie", "Miranda", "Taylor",
    "Abby", "Sarah", "Teagen", "Abby", "Abby",
    "Maddie", "Miranda", "Rosie"
]

names_dictionary = {x:names.count(x) for x in names}
# creating a dictionary keys with the above lists and counting the items

for key, value in names_dictionary.items():
# applying the relevant count of numbers to the dictionary as a value 
    print (key, value)
# printing the value & the keys 