import socket
import time
import sys
from colorama import init, Fore

init(autoreset=True)

def slow_type(text, color=Fore.GREEN, speed=0.02):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
        
    print()

target = 'scanme.nmap.org'
ports = [21, 22, 23, 80, 443]

slow_type(f"[*] Initiating scan on {target}...\n", Fore.CYAN)

for port in ports:
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        slow_type(f"[+] Port {port} is OPEN", Fore.GREEN)
    else:
        slow_type(f"[-] Port {port} is CLOSED", Fore.RED)
    
    s.close

slow_type("\n [✓] Scan complete.", Fore.YELLOW)