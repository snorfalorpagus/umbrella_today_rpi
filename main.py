from led import set_color
from umbrella import umbrella_today
from time import sleep

while True:
    if umbrella_today():
        set_color('BLUE')
    else:
        set_color('GREEN')
    sleep(60 * 30) # 30 minutes
