from vendorclass import Vendor
import udpnet
from machine import Pin

v1 = Vendor(16,17,18,19)
v2= Vendor(15,14,13,12)

v1_run=True
v2_run=True


######
import time
from machine import ADC,Pin
from time import sleep

adc = ADC(Pin(26))
led = Pin("LED",Pin.OUT) #onboard pico w
led2 = Pin(27,Pin.OUT) #onboard pico w
deadline = time.ticks_ms()
######


previoustime=0
newesttime=0
def print_gameloop_time():
    global previoustime, newesttime
    newesttime = time.ticks_us()
    print(newesttime-previoustime)
    previoustime= newesttime





deadline = time.ticks_ms()+300
while(True):
    global address
    #print_gameloop_time()
    message = udpnet.getmessage()
    if (message == b'on'):
        led.on()
        udpnet.sendreply( b'led on')
    if (message == b'off'):
        led.off()
        udpnet.sendreply( b'led off')
    if (message == b'ana'):
        svar = bytes(str(adc.read_u16()), "ascii")
        udpnet.sendreply(svar)
    if (message == b'R1'):
        udpnet.sendreply(b'Run1')
        v1_run=True
    if (message == b'S1'):
        udpnet.sendreply(b'Stop1')
        v1_run=False
    if (message == b'R2'):
        udpnet.sendreply(b'Run2')
        v2_run=True
    if (message == b'S2'):
        udpnet.sendreply(b'Stop2')
        v2_run=False
    if (time.ticks_ms()>deadline):
        #led2.toggle()
        led2.value(not led2.value())
        deadline = time.ticks_ms()+300
    if (v1_run):
        v1.RunSm()
    if v2_run:
        v2.RunSm()
    #print_gameloop_time()

