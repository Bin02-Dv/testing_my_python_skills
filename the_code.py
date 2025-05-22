# number = 0

# while number < 7:
#     number += 3

#     if number == 6:
#         continue

#     print(number)

# number = int(input("Enter a number: "))

# if number%2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an old number")


# shape = input("Enter a shape: ")

# if shape.capitalize() == "Square" '':
#     print("*"*10)
#     print("*"*10)
#     print("*"*10)
#     print("*"*10)
# elif shape.capitalize() == "Triangle":
#     print(" *")
#     print(" *"*2)
#     print(" *"*3)
#     print(" *"*4)
#     print(" *"*5)
#     print(" *"*6)
# else:
#     print(f"{shape} is not available")


# Data Types
"""
String
Integer
float
boolean
    
"""
# number = '7067156212'
# print('+234 -', number)
# print(type(number))

# x = True
# y = False
# print(type(x), type(y))

# # Type casting

# x = input("Enter the first number: ")
# y = input("Enter the second number: ")
# sums = int(x) + int(y)
# print(f"The sum of {x} and {y} is {sums}")

#class Truck:
#    def set__color(self, color):
#        self.__color = color

#    def get__color(self):
#        return self.__color

#obj = Truck()
#obj.set__color("white")
#print(obj.get__color())



# import dns.resolver

# hostname = 'dpg-cn1teptjm4es73evleng-a'
# # answers = dns.resolver.resolve(hostname, 'A')
# for answer in answers:
#     print("IP Address:", answer.to_text())

def calculate_split(total_amount, developer_percent, referrer_percent):
    dev_share = (developer_percent / 100) * total_amount
    ref_share = (referrer_percent / 100) * total_amount
    return dev_share, ref_share

dev, ref = calculate_split(60000, 70, 30)
print(f"Developer: ₦{dev:,.0f}, Referrer: ₦{ref:,.0f}")