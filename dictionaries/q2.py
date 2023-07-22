
# https://favtutor.com/blogs/python-count-occurrences-in-list
# read://https_www.studytonight.com/?url=https%3A%2F%2Fwww.studytonight.com%2Fpython-programs%2Fcounting-the-frequencies-in-a-list-using-dictionary-in-python
# https://pythonexamples.org/python-print-dictionary/

# dictionary
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}
# list
# colours = [
#     "purple",
#     "red",
#     "yellow",
#     "blue",
#     "purple",
#     "orange",
#     "blue",
#     "purple",
#     "orange",
#     "green"
# ]

# # colour name is the "item" and we are instructing python to loop through colours list
# # running a loop to traverve through the list
# for colour_name in colours:
# # loop to read through colour counts and colours to compare / count 
# # To count the frequency, check if the element exists in the dictionary
#     colour_counts[colour_name] +=1
    
#     # this line then tells us to loop through the above temp stored and print out results
# for key, value in colour_counts.items():
#     print(key,":",value)



colours = [
    "orange",
    "purple",
    "blue",
    "yellow",
    "green",
    "green",
    "purple",
    "purple",
    "green",
    "blue",
    "green",
    "orange",
    "purple",
    "blue",
    "green",
    "orange",
    "orange",
    "red",
    "yellow",
    "yellow"
]

for colour_name in colours:
# loop to read through colour counts and colours to compare / count 
# To count the frequency, check if the element exists in the dictionary
    colour_counts[colour_name] +=1
    
    # this line then tells us to loop through the above temp stored and print out results
for key, value in colour_counts.items():
    print(key,":",value)