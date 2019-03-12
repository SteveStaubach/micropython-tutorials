from microbit import *
import music

while True:
    music.pitch(microbit.accelerometer.get_values(), 10)