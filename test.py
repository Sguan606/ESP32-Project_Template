#test.py
from machine import Pin
from machine import Timer
from machine import PWM
from machine import ADC
from machine import UART
import network
import umqtt
import time

# 初始化GPIO_Pin_9
GPIO_Pin_9 = Pin(9,Pin.OUT,None)


# 测试定时器的练手代码1
# def time0_callback(timer):
#     GPIO_Pin_9.value(not GPIO_Pin_9.value())

# 测试定时器的练手代码2
# time0 = Timer(0)
# time1 = Timer(1)
# time0.init(period=500,mode=Timer.PERIODIC,callback = time0_callback)
# time1.init(period=3000,mode=Timer.ONE_SHOT,callback = lambda t:time0.deinit())

# 测试PWM的练手代码1
# pwm0 = PWM(GPIO_Pin_9,freq=1000)

# 测试ADC通道读光敏电阻的练手代码1
# adc0 = ADC(GPIO_Pin_9,atten=ADC.ATTN_11DB)

# 测试just文件操作的练手代码1
# with open("Sguan.txt","w") as just:
#     just.write("JUSTer love JSUT!")
#     just.flush()

# 测试UART串口通信的练手代码1
# uart1 = UART(1,9600,tx=10,rx=9)

# 测试2.4G无线wifi透传的练手代码1
# wlan = network.WLAN(network.STA_IF)

# 测试2.4G无线wifi透传的练手代码2
# def do_connet():
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     if not wlan.isconnected():
#         print("connecting to network...")
#         wlan.connect("星必尘Sguan","sguan12345")
#         while not wlan.isconnected():
#             pass
#     print("network config:",wlan.ifconfig())

# 测试2.4G无线wifi透传的练手代码3
# do_connet()


# 测试mqtt连接客户端服务器的练手代码1
wifi0 = network.WLAN(network.STA_IF)
wifi0.active(True)
wifi0.connect("星必尘Sguan","sguan12345")

# 测试mqtt连接客户端服务器的练手代码2
def mqtt_callback(topic,data):
    print(topic,data)

# 测试mqtt连接客户端服务器的练手代码3
while not wifi0.isconnected():
    pass

# 测试mqtt连接客户端服务器的练手代码4
mqtt0 = umqtt.MQTTClient("连接到服务器需要用的ID","mqtt服务器IP")
mqtt0.set_callback(mqtt_callback)
mqtt0.connect()
mqtt0.subscribe(b"juster")



while True:
#     测试GPIO引脚闪灭的代码
#     GPIO_Pin_9.value(not GPIO_Pin_9.value())
#     time.sleep_ms(700)

#     测试PWM的练手代码2
#     for i in range(1,1023,5):
#         pwm0.duty(i)
#         time.sleep_ms(3)
#     for i in range(1023,1,-5):
#         pwm0.duty(i)
#         time.sleep_ms(3)

#     测试ADC通道读光敏电阻的练手代码2
#     print(adc0.read_u16())
#     time.sleep_ms(50)
    
#     测试just文件操作的练习手代码2
#     with open("boot.py","r") as just:
#         while True:
#             data=just.readline()
#             if not data:
#                 break
#             print(data)
#     time.sleep_ms(5)
    
#     测试UART串口通信的练手代码2
#     uart1.write("I really love my city!")
#     if uart1.any():
#         print(uart1.read(1024))
#     time.sleep_ms(500)
    
#     测试2.4G无线wifi透传的练手代码4
#     if wlan.isconnected():
#         GPIO_Pin_9.off()
#     else:
#         GPIO_Pin_9.on()


#     测试mqtt连接客户端服务器的练手代码5
    mqtt0.check_msg()
    if wifi0.isconnected():
        GPIO_Pin_9.off()
        mqtt0.publish(b"juster","Welcome to my World...Hello my justers!")
    else:
        GPIO_Pin_9.on()
    time.sleep_ms(1)



#     空循环
#     pass

