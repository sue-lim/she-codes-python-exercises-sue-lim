# is_raining = False
# is_cold = True
# print(bool(is_raining))
# print(bool(is_cold))
# print(is_raining)
# print(not is_raining)
# print(is_raining and is_cold)

temperature = 16
# print(temperature < 18)
windchill = 3
# print(windchill > 4)
# print(temperature - windchill < 16)

# name = "Hayley"
# # comparing 2 items
# print(name == "Hayley")

# # # # not equal to
# print(name != "Hayley")

##if statements
is_raining = True
# if is_raining:
#     print("Take an umbrella.")
# else:
#     print("Do not take an umbrella")

# if, elif, else
# if temperature - windchill < 16:
#     print("Take a jumper.")
# elif temperature - windchill > 30:
#     print("Euck, it's hot today, stay home.")
# else:
#     print("Wow, what a lovely day!")

if temperature - windchill < 35 and is_raining:
    print("Just stay home")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    if temperature - windchill < 16:
        print("You'll need a jumper today.")

# a = 1
# b = 2
# if a < b:
#     print("a is less than b")
#     print("a is definitley less than b")
# print("Not sure if a is less than ")
