import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def binary_search_visual(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        clear()
        mid = (low + high) // 2
        for i, val in enumerate(arr):
            if i == mid:
                print(f"[{val}]", end=" ")
            else:
                print(val, end=" ")
        print(f"\n Searching for : {target}")
        print(f" Checking index {mid} (value: {arr[mid]})")
        
        time.sleep(1.5)
        
        if arr[mid] == target:
            
            print(f"\n Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"\n {target} not found.")
    return -1

array = [5, 10, 15, 200, 25, 50, 20, 11, 35]
target = int(input("Enter a target number: "))
binary_search_visual(array, target)