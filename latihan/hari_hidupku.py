# Aplikasi Hari Hidupku v1.0
#
# Aplikasi ini bertujuan menghitung sisa hari-hari hidup kita
# dan dengan demikian menjadi bahan refleksi sederhana
# untuk memohon hati yang bijak dari Sang Kuasa
# 
# Motto: Ajarlah kami menghitung hari kehidupan kami, supaya kami memperoleh hati yang bijak (Mazmur 90:12)
# Referensi: https://www.antaranews.com/berita/1083626/harapan-hidup-orang-indonesia-rata-rata-714-tahun-sebut-kemenkes
# 
# Rencana untuk versi 1.0:
# Menerapkan apa yang telah dipelajari sebelumnya:
# print(), input(), operasi matematika/aritmatika, operator logis if/elif/else
#
# Rencana untuk versi 2.0:
# Tambah fitur menghitung jam yang digunakan untuk berbuat kebajikan,
# waktu yang digunakan untuk merokok, mencek media sosial dlsb.
# Tambah fitur menghitung berapa banyak seseorang makan nasi (kg), daging babi dlsb.
# minum coca cola atau minuman lainnya
# Hitung berapa detakan jantung lagi sampai waktu ajal tiba?
# Hitung berapa kg oksigen kita butuhkan sampai meninggal?

# Salam dan pengantar

print("Salam, sahabat.\n")
print("Setiap orang dari kita cukup sibuk,")
print("karena itu berhentilah sejenak untuk menghirup udara segar")
print("dan panjatkan satu doa singkat ini\n")
print("Tuhan, ajarlah kami menghitung hari kehidupan kami,\nsupaya kami memperoleh hati yang bijak.\n(Mazmur 90:12)\n\n")

# Meminta pengguna memasukkan data

harapan_hidup = 71 # 71 tahun merupakan harapan hidup orang Indonesia menurut tulisan di atas
umur = float(input("Kini tuliskan berapa umur Anda\n(Format: tahun.bulan, mis. 26.4 (26 tahun 4 bulan)\n                           "))

# Mendefinisikan berbagai variable
 
umur_saya = float(umur)
tahun = round((harapan_hidup - umur_saya), 2)
bulan = int(tahun * 12)
minggu = int(tahun * 52)
hari = int(tahun * 365)

# Menampilkan hasil perhitungan kepada pengguna

print("\n=============================================")
print("        Hasil perhitungan python")
print("=============================================\n")
print("Anda memiliki waktu berikut sampai ajal tiba:\n")
print(f"{tahun} tahun")
print(f"{bulan}  bulan")
print(f"{hari} hari")
print("\nLuarbiasa!!")
print(f"Anda masih memiliki {tahun} tahun, {bulan} bulan, {hari} hari\nuntuk berbuat kebajikan.")
print("Berterimakasihlah dan panjatkan secuil doa berikut:\n")
print("Tuhan, ajarlah kami menghitung hari kehidupan kami,\nsupaya kami memperoleh hati yang bijak.\nAmen.\n")
print("Saohagölö.")

