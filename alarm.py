import datetime
import time
from pygame import mixer

alarm_hour = int(input("At what hour do you want to wake up at? "))
alarm_minute = int(input("And at what minute? "))
alarm_second = 0

mixer.init()
mixer.music.load('sound.wav')
mixer.music.set_volume(0.8)

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute and alarm_second == datetime.datetime.now().second:
        mixer.music.play()
        time.sleep(1)
