import time
import sys
import random

lines = [
    "[+] Accessing target system...",
    "[*] Bypassing firewall...",
    "[!] Warning: Trace detected!",
    "[+] Injecting payload...",
    "[*] Upload complete.",
    "[+] Establishing backdoor...",
    "[*] Extraction in progress...",
    "[+] System override successful.",
    "[!] Disconnecting..."
]

def type_like_hacker(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def run_animation():
    for line in lines:
        type_like_hacker(line, delay=random.uniform(0.02, 0.07))
        time.sleep(random.uniform(0.3, 1.2))

if __name__ == "__main__":
    run_animation()