import time
import sys
from colorama import init, Fore

password = '43748BD7'

def slow_type(text, color=Fore.GREEN, speed=0.02):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
        
    print()