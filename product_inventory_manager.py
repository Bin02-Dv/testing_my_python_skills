items = ["Milk", "Bread", "Rice", "Oil"]
prices = [500, 300, 2000, 1500]

budget = int(input(" Enter your Budget: "))
affordable_items = []

for i in range(len(items)):
    item = items[i]
    price = prices[i]

    if price <= budget:
        affordable_items.append(item)
        print(f"You can afford: {item} - ₦{price}")

print(f"\nTotal items you can afford: {len(affordable_items)}")
        
        