import random

# program password acak
# 
# Anda diminta membuat aplikasi password acak
# yang mengunci pintu masuk gudang emas Bank Indonesia
# Password itu dipilih acak dari daftar lima kata
# Layar terminal memberi tahu berapa huruf
# dan meminta pengguna memasukkan huruf terkaan

# variable daftar kata dan tampilan huruf yang diterka
daftar_kata = ["jujur", "setia", "santun", "hormat", "ceria"]

# variable daftar huruf yang akan ditampilkan di layar membantu pengguna
tampilan = []

# memilih satu kata secara acak dari daftar_kata
kata = random.choice(daftar_kata)

# membuat variable jumlah huruf dalam kata
jumlah_huruf = len(kata)

# menulis pengantar di layar
print("Berikut password yang harus Anda terka")

for _ in range(jumlah_huruf):
    tampilan += "_"
print(tampilan)

# pertama diberi kesempatan kepada pengguna
# mencoba terus menerus sampai salah satu huruf ditemukan
# tetapi sesudahnya dia hanya mendapat kesempatan memasukkan huruf
# sebanyak huruf dalam kata yang menjadi password
#
# mencari salah satu huruf untuk memulai proses

start = 0

while start == 0:

    # meminta pengguna menerka satu huruf dari dalam kata yang terpilih
    terkaan = input("Masukkan satu huruf: ")

    # loop untuk membandingkan huruf terkaan dan huruf dalam kata pilihan

    for posisi in range(jumlah_huruf):
        huruf = kata[posisi]
        if huruf == terkaan:
            tampilan[posisi] = huruf
            start = 1

# tampilkan di layar kata yang menjadi password
# dengan letak huruf yang telah ditemukan

print(tampilan)

# sekarang pengguna harus menerka huruf dalam kata password
# sebanyak jumlah huruf dalam kata
# bila pengguna tidak berhasil, maka terminal ditutup.

# pertama kita butuh variable, yang memungkinkan kita membuat batas
# berapa kali pengguna bisa memasukkan huruf terkaan

i = 0

while i < jumlah_huruf:

    # meminta pengguna menerka satu huruf dari dalam kata yang terpilih
    terkaan = input("Terka huruf lainnya: ").lower()

    # melalui fungsi loop kita mencek apakah huruf terkaan
    # sesuai dengan salah satu huruf dalam password
    # bila sesuai kita akan memasukkannya dalam variable tampilan

    for j in range(jumlah_huruf):
        huruf = kata[j]
        if huruf == terkaan:
            # bila terkaan sama dengan huruf dalam password
            # kita masukkan itu dalam variable tampilan
            tampilan[j] = huruf
    # kita perlu mencek apakah semua huruf telah didapatkan
    # walaupun pengulangan belum mencapai maksimum
    # kalau semua huruf telah didapatkan, kita membuka pintu gudang
    if "_" not in tampilan:
        print("Silakan masuk.\nAnda boleh mengambil emas sebanyak Anda mau.")
        i = jumlah_huruf
    
    # kita perlu menaikkan nilai variable i sehingga
    # sehingga pengguna hanya bisa mencoba sekian kali memasukkan huruf
    i += 1

    # kita tampilkan di layar posisi kata yang telah didapatkan
    print(tampilan)

# pada akhir percobaan memasukkan terkaan huruf
# kita mencek apakah masih ada huruf yang belum didapatkan
# untuk memberitahu pengguna bahwa dia tidak mendapat otorisasi masuk gudang
if "_" in tampilan:
    print(tampilan)
    print("Sayang waktu Anda telah habis.\nAnda tidak mendapat otorisasi masuk gudang emas.")
    print("Silakan coba lagi setelah 24 jam!!!")
