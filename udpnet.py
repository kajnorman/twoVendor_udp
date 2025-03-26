import sys
import network
import socket
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ITEK 2nd','2nd_Semester_E24a')
#wlan.connect('Waoo4920_S3N3','pcty7937')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
print(wlan.ifconfig())
time.sleep(1)
#UDPServerSocket = socket.socket() #family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind(("0.0.0.0",5005))
bufferSize = 100
#UDPServerSocket.listen()
print("listening")
address = "empty"
UDPServerSocket.setblocking(False)  #



def getmessage(): #nonblocking
    global  address
    try:
        message,address = UDPServerSocket.recvfrom(bufferSize)
        #fetch message and address of sender
    except:
        message, address = b'',b''
    return message

def sendreply(reply):
    global address
    UDPServerSocket.sendto(reply, address)
