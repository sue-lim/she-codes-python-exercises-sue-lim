# https://realpython.com/iterate-through-dictionary-python/
prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
# }

# for key in quantity:
#     float(prices[key]) * float(quantity[key])
#     price_per_item = round(prices[key],2)
#     total = round(prices[key] * quantity[key],2)
  
#     print(f"{quantity[key]} {key} @ $ {price_per_item} = $ {total}")


quantity = {
    "Baby Spinach": 2,
    "Hot Chocolate": 1,
    "Crackers": 4,
    "Bacon": 0,
    "Carrots": 8,
    "Oranges": 5
}

for key in quantity:
    float(prices[key]) * float(quantity[key])
    price_per_item = round(prices[key],2)
    total = round(prices[key] * quantity[key],2)
  
    print(f"{quantity[key]} {key} @ $ {price_per_item} = $ {total}")
