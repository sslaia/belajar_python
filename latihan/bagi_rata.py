'''
Aplikasi Bagi Rata
Kalkulator pengeluaran kelompok
'''

# Menampilkan keterangan aplikasi

print("Aplikasi Bagi Rata\n")
print("Selamat datang di Bagi Rata\nsatu aplikasi yang menolong Anda menghitung")
print("berapa yang harus dibayar setiap orang\nyang ikut dalam satu aktivitas\n")
print("Silakan memasukkan data berikut:\n")

# Menetapkan berbagai variable yang dibutuhkan

jumlah_peserta = int(input("1. Jumlah peserta : "))
ongkos_taksi = int(input("2. Ongkos taksi   : "))
biaya_minuman = int(input("3. Minuman        : "))
biaya_makanan = int(input("4. Makanan        : "))
tiket_bioskop = int(input("5. Tiket bioskop  : "))
total_sementara = ongkos_taksi + biaya_minuman + biaya_makanan + tiket_bioskop
fee_tambahan = float((5 * total_sementara) / 100)
total_pengeluaran = total_sementara + fee_tambahan
utang_per_orang = total_pengeluaran / 4

# Menampilkan hasil kalkulasi

print("\nTerima kasih. Berikut hasil perhitungan:\n")
print(f"Total pengeluaran : {total_sementara}")
print(f"Fee tambahan (5%) : {fee_tambahan}")
print(f"Utang per orang   : {utang_per_orang}")

print("\nAlisi tafadaya-daya, hulu tafawolo-wolo! Ya'ahowu!\n")

