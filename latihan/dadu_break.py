# permainan dadu sederhana dengan break

import random

MIN = 1
MAX = 6

fazaumba_zui = "y"
nomoro_harizaki = 4

while fazaumba_zui == "y":
    print("Mamazaumba dadu...")
    print("Da'a nomoro harizakimö: ")
    dadu = random.randint(MIN, MAX)
    print(dadu)
    if dadu == nomoro_harizaki:
       print()
       print("Aha. No talo khöu nomoro 4. Harizakiu ma'ökhö!")
       break 
    print()
    fazaumba_zui = input("Lö salania, lö na harizaki.\nOmasi'ö ufuli ufazaumba dadu? (y / l): ")
print()
print("Saohagölö! Ndrege föna zui!")
