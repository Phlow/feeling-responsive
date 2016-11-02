from network import LoRa
import time
import socket

import pycom
pycom.heartbeat(False)

from machine import Pin
p_out = Pin(Pin.exp_board.G16, mode=Pin.OUT)
p_out.toggle()

# Initialize LoRa in LORA mode more params can be given, like frequency, tx power, spreading factor, etc
lora = LoRa(mode=LoRa.LORAWAN, public=True) 
#lora = LoRa(mode=LoRa.LORAWAN, sf=7, tx_power=14)
#lora.BW_125KHZ
#lora.CODING_4_5


# create an OTAA authentication tuple (AppKey, AppEUI, DevEUI)
#char DEVICE_EUI[]  = "0102030405060710";
#char APP_EUI[] = "70B3D57ED00010B5";
#char APP_KEY[] = "3846412DADFD8CE87C1550ED5892698D";
#auth = (bytes([0x38,0x46,0x41,0x2D,0xAD,0xFD,0x8C,0xE8,0x7C,0x15,0x50,0xED,0x58,0x92,0x69,0x8D]), 
#        bytes([0x70,0xB3,0xD5,0x7E,0xD0,0x00,0x10,0xB5]), 
#        bytes([0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x12]))
        
# create an ABP authentication tuple (NwkSKey, AppSKey, DevAddr)
auth = ( 
        bytes([0x7B, 0x38, 0x8D, 0xD4, 0xC4, 0x91, 0x6E, 0xB7, 0xFC, 0xA8, 0x60, 0x65, 0x11, 0x10, 0xF0, 0x42]),
        bytes([0xA8, 0xFD, 0xC5, 0x6B, 0x82, 0x40, 0x07, 0x18, 0x69, 0xBA, 0xAB, 0x74, 0x10, 0x63, 0xCA, 0x74]), 
        0x01000304 )

print("First join attempt")

# join a network using ABP (Activation By Personalization)
print("Joined ", lora.has_joined())
lora.join(activation=LoRa.ABP, auth=auth)

# join a network using OTAA (Over the Air Activation)
#lora.join(activation=LoRa.OTAA, auth=auth, timeout=0)

# wait until the network is joined
i = 0
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
    i = i + 1
p_out.toggle()
print("LoRaWAN joined!")

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

# send some data
msg = "hello"
s.send(msg)
print("Sent 1: ", msg)

i = 0
while i < 100:
    time.sleep(10)
    s.send(msg)
    print("Sent ",i,": ", msg)
    i = i + 1
    

