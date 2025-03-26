from VendorIO import  Trigger_Pin #Nickelreturn, Itemreturn,
from machine import Pin
from time import sleep

S0 = 0
S5 = 5
S10 = 10
S15 = 15
S20 = 20



class Vendor:
    def __init__(self, n_pin, d_pin,ri_pin,rn_pin):
        self.R = Pin(ri_pin, Pin.OUT)
        self.C = Pin(rn_pin, Pin.OUT)
        n = Pin(n_pin, Pin.IN, Pin.PULL_DOWN)
        d = Pin(d_pin, Pin.IN, Pin.PULL_DOWN)
        self.nt = Trigger_Pin(n)
        self.dt = Trigger_Pin(d)
        self.Tilstand = S0  # her starter maskinen
        self.GlTilstand = S0  # her starter maskinen
        print("Møntindkast initialiserer")
        self.Nickelreturn()
        self.Itemreturn()

    def Nickelreturn(self):
        self.C.on()
        sleep(0.5)
        self.C.off()

    def Itemreturn(self):
        self.R.on()
        sleep(0.5)
        self.R.off()

    def nick(self):
        return self.nt.Triggered()
        return self.nt.Triggered()
        # or False

    def dime(self):
        return self.dt.Triggered()
        # or False

    def RunSm(self):
        self.GlTilstand = self.Tilstand
        if self.Tilstand == S0:
            if self.dime():
                self.Tilstand = S10
            if self.nick():
                self.Tilstand = S5
        elif self.Tilstand == S5:
            if self.dime():
                self.Tilstand = S15
            if self.nick():
                self.Tilstand = S10
        elif self.Tilstand == S10:
            if self.dime():
                self.Tilstand = S20
            if self.nick():
                self.Tilstand = S15
        elif self.Tilstand == S15:
            # release item
            self.Itemreturn()
            self.Tilstand = S0
        elif self.Tilstand == S20:
            # release change
            self.Nickelreturn()
            self.Tilstand = S15
        if (self.GlTilstand != self.Tilstand):
            print(self.Tilstand)



