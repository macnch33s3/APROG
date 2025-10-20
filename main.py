from microbit import *

# APROG Willkommensprogramm für micro:bit
# Flashen mit "ufs put main.py"

a = 10
b = 6

if a > b:
    groesstes = a
else:
    groesstes = b

display.show(groesstes)