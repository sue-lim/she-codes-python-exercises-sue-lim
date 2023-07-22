# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box" , "kong"]
# print(len(chilli_wishlist))
# print(chilli_wishlist[3])
# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[-1])
# print(chilli_wishlist[0:2])
# print(chilli_wishlist[1:3])

# # insert into position 1 carrot 
# chilli_wishlist[1] = 'carrot'
# print(chilli_wishlist)

# chilli_wishlist[0] = 'dog'
# print(chilli_wishlist)

# add dig mat to the end 
# chilli_wishlist.append('dig mat')

# # add these to the end 
# chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])

# # amend to position 1
# chilli_wishlist.insert(1, 'peanut butter')
# # print(chilli_wishlist)

# # without providing details as to which one we want to delete, it will pop it from the end
# chilli_wishlist.pop()

# # this removed the list item in position 2 which was chicken 
# chilli_wishlist.pop(2)

# # or you can specify the string you want to remove 
# chilli_wishlist.remove('kong')

# # adding a new item we use insert with 2 from the end
# chilli_wishlist.insert(-2, 'flowers')

# # remove the item from the 3 position 
# chilli_wishlist.pop(3)

# # remove igloo from the list 
# chilli_wishlist.remove('igloo')

# print(chilli_wishlist)

# if "kong" in chilli_wishlist:
#     print("Chilli would like a kong.")
# else:
#     print("Chilli doesn't feel like playing fetch.")
# if len (chilli_wishlist)> 8:
#     print("Chilli wants a lot of stuff!")

##### if statement for when the item is not in the list and you want to add it #####
# if "blueberries" is not chilli_wishlist:
#     chilli_wishlist.append("blueberries")
#     print(chilli_wishlist)

# # Sublists
chilli_wishlist = [
    ['igloo'],
    ['donut toy','tennis ball', 'crocodile toy'], 
    ['chicken', 'peanut butter'],
    ['cardboard box', 'kong', 'dig mat']
    ]
# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[2])
# print(chilli_wishlist[3])


# message = f"there are {len(chilli_wishlist)} in this list"
# print (message)
print(chilli_wishlist[0])
print(chilli_wishlist[1])
print(chilli_wishlist[2])
print(chilli_wishlist[3])

# sublist 1, insert sugar into position 1
chilli_wishlist[1].insert(1,'sugar')
print(chilli_wishlist[0])
print(chilli_wishlist[1])
print(chilli_wishlist[2])
print(chilli_wishlist[3])