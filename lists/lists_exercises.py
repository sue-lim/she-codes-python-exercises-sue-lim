# print('###################Question_Two###################')
# foods = [["orange","apple","banana","strawberry","grape","blueberry"],
# ["carrot", "cauliflower", "pumpkin"],
# ["passionfruit","mango","kiwifruit"]]
# # print(foods)
# print(foods[0][0])
# print(foods[0][2])
# print(foods[2][2])
# print(foods[1])
# print(foods[2])
# print(foods[1][2])


# print('###################Question_Two###################')
# mailing_list = [["Chilli", "chilli@thechihuahua.com"],
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Ivy", "noreply@goldendreamers.xyz"]]

# # for = loop through mailisting list
# for items in mailing_list:
#     # print all items in column 0 and end with ':'
#     print (items[0], end = ': ')
#     # print all items in column 1, corrosponding with the items in column 0
#     print (items[1])

# print('###################Question_Three###################')
# names_list = []
# print(f"Current name list {names_list}")
# new_name = input("Enter a name: \n")
# names_list.append(new_name)
# print(f'Updated names list {names_list}')

# new_name = input("Enter a name: \n")
# names_list.append(new_name)
# print(f'Updated names list {names_list}')

# new_name = input("Enter a name: \n")
# names_list.append(new_name)
# print(f'Updated names list {names_list}')

# names_list = []
# # for loop to loop through 3 times and amend the names into the names_list
# for i in range(3):
#     name = input("Enter name: ")
#     names_list.append(name)

# print(names_list)
print('###################Question_Four###################')
code_list_a = [1, 2, 3]
code_list_b = [4, 5, 6]
code_list_c = [7, 8, 9] 
code_list_d = [] 
code_list_e = []

print(f"{code_list_a} {code_list_b} {code_list_c}")

code_list_a.append(code_list_b.pop(-3))
code_list_a.append(code_list_b.pop(-2))
code_list_a.append(code_list_b.pop(-1))
code_list_a.append(code_list_c.pop(-3))
code_list_a.append(code_list_c.pop(-2))
code_list_a.append(code_list_c.pop(-1))
print(code_list_a)




