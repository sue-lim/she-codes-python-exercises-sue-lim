##GREETING FUNCTION##
# # def create_greeting(name):
#     greeting = f"Hello, {name}!"
#     return greeting

# print(create_greeting("Chilli"))
# print(create_greeting("Ivy"))
# print(create_greeting("Remus"))

##CHALLENGE takesanintegerasaparameterandreturnsthatintegermultiplied by 3##

# def create_number(num):
#     number = int(num*3)
#     return number

# print(create_number(3))
# print(create_number(2))
# print(create_number(6))
# n = input("Please enter value in centimeters: ")
# float_number = float(n)
# def convert_cm_to_in(length_cm):
#     length_in_inches = length_cm / 2.54
#     return length_in_inches
# print(convert_cm_to_in(float_number))

# n = input("Please enter value in inches: ")
# float_number = float(n)
# def convert_in_to_cm(length_in):
#     length_in_cm = length_in * 2.54
#     return length_in_cm
# print(f"Length is {convert_in_to_cm(float_number)} cm")

def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean
print(calculate_mean(3, 4))