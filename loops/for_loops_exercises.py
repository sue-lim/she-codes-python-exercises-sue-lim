print("##########QUESTION 1 A ##########")

n = int(input("Enter a number: "))

for number in range(n):
    print(f"{n} * {number+1} = {(n)*(number+1)}")

print("##########QUESTION 2 ##########")

n = int(input("Enter a number: "))

for x in range(3,22,n*3): 

        print(x)


# print("##########QUESTION 3 ##########")

# random_numbers_1 = [3, 5, 9, 1] 
# total_1 = 0
# for x in range(0,len(random_numbers_1)):
#    total_1 = total_1 + random_numbers_1[x]
# print(total_1)   

# random_numbers_2 = [-3, -5, 9, 1] 
# total_2 = 0
# for x in range(0,len(random_numbers_2)):
#    total_2 = total_2 + random_numbers_2[x]
# print(total_2)   

# random_numbers_3 = [] 
# total_3 = 0
# for x in range(0,len(random_numbers_3)):
#    total_3 = total_3 + random_numbers_3[x]
# print(total_3)   

print("##########QUESTION 4 ##########")

mailing_list = [
["Chilli", "chilli@thechihuahua.com"],
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Ivy", "noreply@goldendreamers.xyz"],
]

# print(mailing_list)
for email in mailing_list:
    print (email[0], end = ': ')
    print (email[1])
    

 
    

