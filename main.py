import time
from plyer import notification
total=0
while True and total!=3:
    print("SIP SOME WATER !!!!!")
    notification.notify(title="Hey drink some water",message="you drink some water ")
    total+=1
    time.sleep(3)
