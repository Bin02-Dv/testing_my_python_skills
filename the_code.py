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


shape = input("Enter a shape: ")

if shape.capitalize() == "Square":
    print("*"*10)
    print("*"*10)
    print("*"*10)
    print("*"*10)
elif shape.capitalize() == "Triangle":
    print(" *")
    print(" *"*2)
    print(" *"*3)
    print(" *"*4)
    print(" *"*5)
    print(" *"*6)
else:
    print(f"{shape} is not available")