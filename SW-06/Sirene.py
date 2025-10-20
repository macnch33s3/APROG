# Zusatzbeispiel-OOP für Microbit
# Sirenen-Simulation
from microbit import *
import music

class Syrene():
    def __init__(self, low, high, dauer):
        self.ltone = low
        self.htone = high
        self.time = dauer

    def fasten(self):
        if button_a.is_pressed():
            self.time -= 50
        elif button_b.is_pressed():
            self.time += 50
        else:
            self.time = self.time

    def pitch(self):
        if accelerometer.is_gesture('left'):
            self.ltone -= 50
            self.htone -= 50
        elif accelerometer.is_gesture('right'):
            self.ltone += 50
            self.htone += 50

    def play(self):
        music.pitch(self.ltone)
        sleep(self.time)
        music.pitch(self.htone)
        sleep(self.time)

    def check(self):
        if pin_logo.is_touched():
            return False
        else:
            return True

    def stop(self):
        speaker.off()

s = Syrene(440, 500, 1000)

run = True
while run:
    s.play()
    s.fasten()
    s.pitch()
    run = s.check()
s.stop()