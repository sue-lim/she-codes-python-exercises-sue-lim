############################ VARIABLES & INPUTS ############################

# print('#####Variables and User Input#####')
# name = input("What is your name? ")
# hobby = input("What is your favourite hobby? ")
# print(f"This is {name}, who likes {hobby}.")

# age = input(f"Hi {name}, how old are you? ")
# years_until_100 = 100 -int(age)
# print(f"Wow, {name}! You'll be 100 in {years_until_100} years!")

############################
# day = "Saturday"
# print(str(day))

# message = f"Today is {day}!"
# print(message)
############################

# name = input("What is your name? ")
# day = input("What day is it today? ")
# print(str(day))
# month = input("What is the current month? ")

# # weather = input("How is the weather today? ")
# # print(f"Hi {name}. It is {day} and the weather is {weather}")
# print(f"Hi {name}. It is {day} and we are in {month}")

############################ INTEGERS ############################
# Run distance in m
# run1_dist = 1400
# run2_dist = 1800

# # # Addition
# # total_distance = run1_dist + run2_dist

# # Floats
# # Run distance in km
# run3_distance = 1.7
# run4_distance = 1.35

# # Addition
# total_distance = run3_distance + run4_distance
# print(int(total_distance))
# print(float(total_distance))

# print(f"{run1_dist / 1000} m")
# print(f"{run4_distance * 1000} km")

# goal_distance = (total_distance) - run1_dist
# print(int(goal_distance))

########################################################
run5_dist = "5000"
# the below will produce an error as we have not provided instructions on whether it is a str or integer
# print(run5_dist + 3)

# the below will add a 3 at the end of 50003
# print(run5_dist + "3")

# this will print 5000 x 3 times
# print(run5_dist * 3)

# this will error as 3.0 is a float
# print(run5_dist * 3.0)

# this is the correct solution as it is instructing that the digits are numbers
print(int(run5_dist) + 3)

# this seems to have done nothin but it has given the instructions for the number to be printed as a string not an integer.
print(str(3))
