import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

stack = []
actions = ['Add Plate1', 'Add Plate2', 'Add Plate3']

print("STACK - Last In, First Out (LIFO) \n")

for action in actions:
    stack.append(action)
    clear()
    print("Stack:", stack)
    time.sleep(1.2)
    
queue = []
actions = ['Alamin', 'Amina', 'Kamal', 'Baffa']

for person in actions:
    queue.append(person)
    clear()
    print("Queue:", queue)
    time.sleep(1)

while queue:
    served = queue.pop(0)
    clear()
    print(f"Serving: {served}")
    print("Queue:", queue)
    time.sleep(1.2)