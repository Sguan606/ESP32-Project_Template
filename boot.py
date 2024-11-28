# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import UART
import os
uart = UART(0, 115200)
os.dupterm(uart)

print("Hello my Jsut!")
