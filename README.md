# twoVendor_udp
To "møntautomater" kører i et gameloop med frivillig tidsdeling.
en UDP-backend kan fjernstyre hvisse funtioner i systemet.

følgende opgave er næsten løst:

Med udgangspunkt i wokwi-løsningen af to møntmaskiner herunder:
https://wokwi.com/projects/426349534630713345
Ønskes følgende designet,implementeret og testet.

Udføres uden brug af interrupts/asyncio/2kerner/chatgpt/

Udføres i samarbejde og diskusion.


Afprøv 2 stk kørende Vendor-maskiner. på wokwi

Onboard pico Led skal samtidigt blinke  2gg i sek

Få den til at køre på hardware pico.

Få systemet til at lytte ublokerende på UDP

Følgende UDP-komandoer skal medføre følgende aktioner

Komando	/ aktion :
### run1	/ start vendor1
### stop1	/ stop vendor1
### run2	/ start vendor2
### stop2	/ stop vendor2
### count1 / Skal returnere antallet af udleverede items.

 

Brug nogen timer og aflever bevis for hvor langt du nåede i processen
