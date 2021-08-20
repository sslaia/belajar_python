# permainan dadu sederhana dengan break

import random

MIN = 1
MAX = 6

lempar_dadu = "y"
nomor_dadu = 4

while lempar_dadu == "y":
    print("Sedang melempar dadu...")
    print("Inilah nomor keberuntunganmu hari ini: ")
    dadu = random.randint(MIN, MAX)
    print(dadu)
    if dadu == nomor_dadu:
       print()
       print("Selamat. Anda mendapat nomor keberuntungan 4!")
       break 
    print()
    lempar_dadu = input("Anda belum beruntung. Mau mencoba sekali lagi? (y / t): ")
print()
print("Trims! Sampai lain kali!")
