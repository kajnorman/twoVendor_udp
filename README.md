# twoVendor_udp
To "møntautomater" kører i et gameloop med frivillig tidsdeling.
en UDP-backend kan fjernstyre hvisse funtioner i systemet.

Med udgangspunkt i wokwi-løsningen af to møntmaskiner herunder:
 https://wokwi.com/projects/426349534630713345

Er følgende designet,implementeret og testet.

Udført uden brug af interrupts/asyncio/2kerner/chatgpt/

2 stk kørende Vendor-maskiner.

Onboard pico Led blinker  2gg i sek

Systemet tlytter ublokerende på UDP

Følgende UDP-komandoer skal medfører følgende aktioner

Komando	/ aktion :
### run1	/ start vendor1
### stop1	/ stop vendor1
### run2	/ start vendor2
### stop2	/ stop vendor2
### count1 / Skal returnere antallet af udleverede items.
