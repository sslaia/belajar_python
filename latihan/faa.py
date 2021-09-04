# Menetapkan berbagai variable
#
nama_a = input("Tuliskan nama depan Anda (tanpa marga)\n")
nama_b = input("Tuliskan nama depan pasangan Anda (tanpa marga)\n")
umur_a = input("Tuliskan umur Anda (angka bulat tahun)\n")
umur_b = input("Tuliskan umur pasangan Anda (angka bulat tahun)\n")
pendidikan_a = input("Pendidikan terakhir Anda (SD: 1; SMP: 2; SMA: 3; PT: 4)\n")
pendidikan_b = input("Pendidikan terakhir pasangan Anda (SD: 1; SMP: 2; SMA: 3; PT: 4)\n")
huruf_khusus = ["n", "s", "t"]

# Menghitung poin nama
#
# Membuat variable poin_nama
poin_nama_a = 0
poin_nama_b = 0
poin_nama = 0

# Mengadakan perhitungan dengan menggunakan for loop
for huruf in huruf_khusus:
    if huruf in nama_a:
        poin_nama_a = 1
    else:
        poin_nama_a = 3

    if huruf in nama_b:
        poin_nama_b = 1
    else:
        poin_nama_b = 3

if poin_nama_a + poin_nama_b == 6:
    poin_nama = 3
if poin_nama_a + poin_nama_b == 4:
    poin_nama = 2
else:
    poin_nama = 1

# Menampilkan poin dari perbandingan nama
print(f"Total poin perbadingan nama: {poin_nama}")

# Alternatif kedua
# for huruf in huruf_khusus:
#     if huruf not in nama_a and huruf not in nama_b:
#         poin_nama = 3
#     elif huruf in nama_a and huruf not in nama_b:
#         poin_nama = 2
#     elif huruf in nama_b and huruf not in nama_a:
#         poin_nama = 2 
#     else:
#         poin_nama = 1

# Menampilkan poin dari perbandingan nama
# print(f"Total poin nama: {poin_nama}")


# Menghitung poin perbedaan umur
#
# Membuat variable hasil perhitungan umur
poin_umur = 0

selisih_umur = int(umur_a) - int(umur_b)
print(f"Selisih umur: {abs(selisih_umur)}")

if abs(selisih_umur) <= 5:
    poin_umur = 3
elif abs(selisih_umur) <= 10:
    poin_umur = 2
else:
    poin_umur = 1

# Menampilkan poin dari umur
print(f"Poin dari umur: {poin_umur}")

# Menghitung poin pendidikan
#
# Membuat variable hasil perhitungan pendidikan
poin_pendidikan = 0

# Mengadakan kalkulasi
if int(pendidikan_a) == int(pendidikan_b):
    poin_pendidikan = 3
elif int(pendidikan_a) - int(pendidikan_b) == 1 or int(pendidikan_b) - int(pendidikan_a) == 1:
    poin_pendidikan = 2
else:
    poin_pendidikan = 1

# Menampilkan poin pendidikan
print(f"Poin dari pendidikan: {poin_pendidikan}")


# Menghitung total poin pasangan

poin_total = poin_nama + poin_umur + poin_pendidikan
print(f"Total poin pasangan: {poin_total}")

# Menampilkan pesan prospek pasangan

if poin_total == 3:
    print("Prospek pasangan Anda: lampu merah")
elif poin_total < 6:
    print("Prospek pasangan Anda: lampu kuning")
else:
    print("Prospek pasangan Anda: lampu hijau")


