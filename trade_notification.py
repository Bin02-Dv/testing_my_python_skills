import time
from datetime import datetime
import winsound
from plyer import notification

def alert():
    
    winsound.Beep(1000, 1000)
    
    notification.notify(
        title="15-minutes Alert",
        message=f"Sir it's time to check the trade, the time is {datetime.now().strftime("%H:%M:%S")}",
        timeout=10
    )

print("Alert system started... You will be notified every 15 minutes.")

try:
    while True:
        alert()
        time.sleep(15 * 60)
except KeyboardInterrupt:
    print("\nAlert system stopped manually.")