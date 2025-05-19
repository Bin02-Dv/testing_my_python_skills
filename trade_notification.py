import time
import winsound
from datetime import datetime
from plyer import notification

def alert():
    
    winsound.Beep(1000, 1000)
    
    notification.notify(
        title="Trading Notification",
        message="Sir it's time to enter your trade...",
        timeout=10
    )

print("Notification has started...")

try:
    while True:
        alert()
        time.sleep(15 * 60)
except KeyboardInterrupt:
    print("Notification has stoped!!")