from microbit import *

# APROG Willkommensprogramm für micro:bit
# Flashen mit "ufs put main.py"

while True:
    display.clear()
    display.scroll("Willkommen in APROG!", delay=80)
    display.show(Image.HEART)
    sleep(1000)
