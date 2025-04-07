shopping_cart = {
    "Laptop Bag": 4500,
    "Wireless Mouse": 3000,
    "Notebook": 1200,
    "Pen": 600,
    "USB Drive": 2500
}

total = sum(shopping_cart.values())
discount = 0

if total > 10000:
    discount = total * 0.10
    total -= discount


print("Shopping Cart: ")
for item, price in shopping_cart.items():
    print(f"{item}: ₦{price}")

print(f"\nDisount Applied: ₦{int(discount)}")
print(f"Total to pay: ₦{int(total)}")