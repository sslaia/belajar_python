# permainan dadu sederhana

import random

MIN = 1
MAX = 6

fazaumba_zui = "y"

while fazaumba_zui == "y":
    print("Mamazaumba dadu...")
    print("Da'a nomoro harizakimö: ")
    dadu = random.randint(MIN, MAX)
    print(dadu)
    print()
    fazaumba_zui = input("Omasi'ö ötohugö? (y / l): ")
print()
print("Ndrege da'ö ua he! Saohagölö manö.")

