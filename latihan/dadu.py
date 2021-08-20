# permainan dadu sederhana

import random

MIN = 1
MAX = 6

lempar_dadu = "y"

while fazaumba_zui == "y":
    print("Sedang melempar dadu...")
    print("Inilah nomor keberuntunganmu hari ini: ")
    dadu = random.randint(MIN, MAX)
    print(dadu)
    print()
    lempar_dadu = input("Mau lempar dadu lagi? (y / t): ")
print()
print("Terima kasih. Sampai lain kali.")

