# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import UART
import os
uart1 = UART(1, 115200)
os.dupterm(uart)

print("Hello my Jsut!")
