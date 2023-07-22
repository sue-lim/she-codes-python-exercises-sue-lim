# def create_greeting(name):
#     greeting  = f"Hello, {name}"
#     return greeting

# print(create_greeting("Chilli"))
# print(create_greeting("Daisy Sparkles"))

# challenge is to create something that returns by 3
# def do_multiplication(num):
#     multiply = num * 3
#     return multiply
# print(do_multiplication(3))
# print(do_multiplication(10))

# creating a function "convert_cm_to_inches"
# def convert_cm_to_in (length_cm):
#     # create the variable 
#     length_in_inches = length_cm / 2.54
#     return length_in_inches

# #print string + function + value
# print(f"{convert_cm_to_in(20)} inches")

# # creating a function "convert_in_to_cm"
# def convert_in_to_cm(length_in):
#     # create the variable 
#     length_in_cm = length_in * 2.54
#     return length_in_cm

# #print string + function + value
# print(f"{convert_in_to_cm(6)} cm")

# def calculate_mean(a, b):
#     total = int(a) + b 
#     multiply = a * b
#     mean = total / 2
#     return [mean, total, multiply]

# print(calculate_mean(3,4)) 

#print(f"{total},{total}, {multiply}")

# def sayhello(name):
#     print(f"Hello {name}")
# sayhello("Sue")
# sayhello("John")
# sayhello("Bob")

# def mult(num1, num2):
#     return(num1*num2)
    
# mult(5,10)
# mult(1,8)
# mult(150,203)
# percentage=mult(15,5)/100 

# print(f"the product of the two numbers ({mult} 15,5)")

def getprice(flower):
    if flower=="rose":
        return 3.50
    elif flower=="tulip":
        return 2.5
    elif flower=="orchid":
        return 25
    
def calculatecost(quantity, priceperunit):
    return quantity*priceperunit
price=getprice('tulip')
totalsellingprice=0
flower=input("what is the first type of flowers? ")
units=input("how many of these are sold? ")
units=int(units)
price=getprice(flower)
totalsellingprice=calculatecost(units,price)

# print(int(calculatecost(1,5)))  

# print(len("hello"))
# countries=["China","Japan","United States","United Kingdom","India", "Korea"]
# print(len(countries))

# name=input("Enter your name: ")
# for x in range(len(name)):
#     print(name[x])
    
# test_scores=(50,100,97,75,80)
# print(sum(test_scores))

# dir[(1,2,32)]

# class bird:
#     wings=2
#     legs=2
#     beak=1
#     def __init__(self, name, weight, color):
#         self.species=name
#         self.weight=weight
#         self.color=color
#     def eat(self):
#         print("I am eating")
#     def make_sounds(self):
#         print("I am chirping")
#     def fly(self):
#         print("I am flying")
#     def speak(self):
#         print(f"Hi, I am a {self.species}. I have {self.legs} legs, {self.wings} wings and {self.beak} beak")
#         print(f"I weigh {self.weight} grams and am {self.color} in color")
        
# bluebird=bird('bluebird', 30, 'blue')
# sparrow=bird('sparrow', 30, 'brown')

# print(bluebird.legs)
# print(sparrow.legs)

# sparrow.speak()
# bluebird.speak()
        



