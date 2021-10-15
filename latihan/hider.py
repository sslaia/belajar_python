#Membuat program kasir sederhana untuk TOKO HIDER
def garis():
    print("-------------------------------------------------------------------------")
def bintang():
    print("*************************************************************************")
garis()
print("TOKO HIDER\n".center(75))
print("Hilifalawu, Kec. Maniamolo, Kab. Nias Selatan (HP: 085 222 000 000)".center(75))
bintang()
print("Pilihan Menu")
print("-------------------------")
print("1. Gore Gae -> Rp 1.000")
print("2. Gado-Gado -> Rp 1.500")
print("3. Kopi susu -> Rp 2.000")
print("4. Teh Manis -> Rp 2.500")
print("-------------------------")
Kasir=input("Nama Kasir : ")
Tanggal=input("Masukkan tanggal : ")
pilih=int(input("Masukkan menu pilihan: "))
if pilih==1:
    print("Gore Gae dengan harga Rp 1.000")
    jumlah=int(input("Jumlah Pesanan: "))
    print("")
    total=jumlah*1000
    print("Total Harga.................:",total)
elif pilih ==2:
    print("Gado Gado dengan harga Rp 1.500")
    jumlah=int(input("Jumlah Pesanan: "))
    print("")
    total=jumlah*1500
    print("Total Harga.................:",total)
elif pilih==3:
    print("Kopi Susu dengan harga Rp 2.000")
    jumlah=int(input("Jumlah Pesanan: "))
    print("")
    total=jumlah*2000
    print("Total Harga.................:",total)
elif pilih==4:
    print("Teh Manis dengan harga Rp 2.500")
    jumlah=int(input("Jumlah Pesanan: "))
    print("")
    total=jumlah*2500
    print("Total Harga.................:",total)
else:
    stop=True
    print("")
    print("Menu tidak tersedia---->Silahkan pilih menu yang lain")
    print("")
    print("*****Saohagolo*****")
    exit()
bayar=int(input("Pembayaran Tunai ...........: "))
if total >= 100000:
    disc_Member=int(total*0.20)
    disc_Non_Member=int(total*0.15)
    Member=int(input("Masukkan Kode Member........: "))
    if Member>=1:
        print("Diskon 20%..................:",disc_Member)
        kembali=int(bayar-(total-disc_Member))
        print("Kembali ....................:",kembali)
    else:
        print("Diskon 15%..................:",disc_Non_Member)
        kembali=int(bayar-(total-disc_Non_Member))
        print("Kembali ....................:",kembali)
elif total >= 75000:
    disc_Member=int(total*0.10)
    disc_Non_Member=int(total*0.075)
    Member=int(input("Masukkan Kode Member.......: "))
    if Member>=1:
        print("Diskon 10%..................:",disc_Member)
        kembali=int(bayar-(total-disc_Member))
        print("Kembali ....................:",kembali)
    else:
        print("Diskon7.5%..................:",disc_Non_Member)
        kembali=int(bayar-(total-disc_Non_Member))
        print("Kembali ....................:",kembali)
elif total >= 50000:
    disc_Member=int(total*0.05)
    disc_Non_Member=int(total*0.025)
    Member=int(input("Masukkan Kode Member........: "))
    if Member>=1:
        print("Diskon  5%..................:",disc_Member)
        kembali=int(bayar-(total-disc_Member))
        print("Kembali ....................:",kembali)
    else:
        print("Diskon2.5%..................:",disc_Non_Member)
        kembali=int(bayar-(total-disc_Non_Member))
        print("Kembali ....................:",kembali)
else:
    kembali=int(bayar-(total))
    print("Kembali ....................:",kembali)
print("")
print("Terima Kasih atas kunjungan anda, silahkan berbelanja kembali".center(75))
print("******SAOHAGOLO*****".center(75))
garis()


