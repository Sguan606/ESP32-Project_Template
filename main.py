#main.py
#Basic files written by MicroPython based on Thonny.
#You are supposed write your own python file in it!
import machine
from network import WLAN
import time
from simple import MQTTClient


DISCONNECTED = 0
CONNECTING = 1
CONNECTED = 2
HOST = "yourSpecificEndPointHere.iot.eu-west-1.amazonaws.com"
TOPIC = "myThingName"
state = DISCONNECTED
connection = None

def pub_msg(msg):
    global connection
    connection.publish(topic=TOPIC, msg=msg, qos=0)
    print('Sending: ' + msg)

def run():
    global state
    global connection
    while True:
        while state != CONNECTED:
            try:
                state = CONNECTING
                connection = MQTTClient(client_id=TOPIC, server=HOST, port=8883, keepalive=10000, ssl=True, ssl_params={"certfile":"/flash/cert/cert.pem", "keyfile":"/flash/cert/privkey.pem", "ca_certs":"/flash/cert/aws-iot-rootCA.ca"})
                connection.connect()
                state = CONNECTED
            except:
                print('Could not establish MQTT connection')
                time.sleep(0.5)
                continue

        print('MQTT LIVE!')

        while state == CONNECTED:
            msg = '{"device_id":"some_id", "data":"some_data"}'
            pub_msg(msg)
            time.sleep(2.0)

          
  
