Groceries = {
"baby_spinach": 2.78, 
"hot_chocolate" : 3.70, 
"crackers": 2.10, 
"bacon": 9.00, 
"carrot": .56,
"oranges": 3.08, 
}

print(Groceries)

# this will print the price of bacon 
print(Groceries["bacon"])

# this will delete the crackers from the list
del Groceries["crackers"]
print(Groceries)

# this will amend the price of avocadoes 
Groceries['avocadoes']=1.00
print(Groceries)

# amend hot chocolate price 
Groceries['hot_chocolate']=2.70
print(Groceries)

# groceries to items can be seperated as 2 values vs specifiying eg like indexing 
# you can use this for sublists vs using lists and storing quite a few things 
for item, price in Groceries.items():
    print (f"{item}: ${price}")
    
# another way to display 
for item in Groceries:
    print(f"{item}: ${Groceries[item]}")