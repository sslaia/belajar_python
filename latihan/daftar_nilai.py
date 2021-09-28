# Ini adalah aplikasi memasukkan nilai ijazah siswa ke dalam database
#
# Sekedar tampilan judul
judul = '''
    \_/
  --(_)--  .
    / \   /_\\
          |Q|
    .-----' '-----. 
   /___[ SEKOLAH]__\\
    | [] .-.-. [] | 
  ..|____|_|_|____|..

    Selamat datang di

SD Negri 1, Hiliwalangi'adu

Aplikasi Nilai Ijazah Siswa


'''
# Sekedar tampilan bak catatan kaki
catatan_kaki = '''
Belajar itu seumur hidup

       _.-'`'-._
    .-'    _    '-.
     `-.__  `\\_.-'
       |  `-``\\|
       `-.....-A
               #
               #
'''

# Mendefinisikan berbagai fungsi

# Fungsi untuk memasukkan data ke database
def simpan_data(nama, gender, nilai):
    daftar_nilai.append({"nama": nama, "gender": gender, "nilai": nilai})
    print("Trims. Data telah ditambahkan!")

# Formulir memasukkan data
def formulir_memasukkan_data():
    nama =   input("Nama  : ")
    gender = input("Gender: ")
    nilai =  input("Nilai : ")

    simpan_data(nama, gender, nilai)

# Menghitung nilai rata-rata
def hitung_nilai_rata():
    total_nilai = 0
    for i in daftar_nilai:
        total_nilai += int(i["nilai"])
    
    return total_nilai / len(daftar_nilai)

# Mencari siswa dengan nilai tertinggi
def cari_nilai_tertinggi():
    nilai = daftar_nilai[0]["nilai"]
    nama = daftar_nilai[0]["nama"]

    for i in daftar_nilai:
        nilai_siswa = i["nilai"]
        if nilai_siswa > nilai:
            nilai = nilai_siswa
            nama = i["nama"]
    return nama, nilai

# Mencari siswa dengan nilai terrendah
def cari_nilai_terrendah():
    nilai = daftar_nilai[0]["nilai"]
    nama = daftar_nilai[0]["nama"]

    for i in daftar_nilai:
        nilai_siswa = i["nilai"]
        if nilai_siswa <= nilai:
            nilai = nilai_siswa
            nama = i["nama"]
    return nama, nilai


# Program mulai dari sini

# Mendeklarasikan nama daftar
daftar_nilai = []

# Mencetak judul
print(judul)

# Menampilkan formulir pemasukkan data
# Buat variable untuk mengontrol selesai/maju
terus = True

# Tampilkan formulir dan pesan setelah selesai
while terus:
    formulir_memasukkan_data()

    selesai = input("Terus? y/t ")

    if selesai == "y":
        print("*" * 20)
        terus = True
    elif selesai == "t":
        print("*" * 20)
        print("Terima kasih.")
        terus = False
    else:
        print("Silakan ketik y atau t")

print()
print(f"Inilah data yang telah masuk dalam database: \n{daftar_nilai}")
print()


# Menghitung nilai rata-rata
# Buat variable
nilai_rata = hitung_nilai_rata()

# Tampilkan di layar nilai rata-rata
print(f"Nilai rata-rata  : {round(nilai_rata, 2)}")

# Mencari siswa dengan nilai tertinggi dan tanpilkan di layar
print(f"Nilai tertinggi  : {cari_nilai_tertinggi()[0]} (nilai: {cari_nilai_tertinggi()[1]})")

# Mencari siswa dengan nilai terrendah dan tampilkan di layar
print(f"Nilai terrendah  : {cari_nilai_terrendah()[0]} (nilai: {cari_nilai_terrendah()[1]})")
print("*" * 20)

# Mencetak catatan kaki
print(catatan_kaki)





# Sekedar isi database kalau diperlukan
# daftar_nilai.append({"nama": "Siti", "gender": "perempuan", "nilai": 9})
# daftar_nilai.append({"nama": "Budi" , "gender": "laki-laki", "nilai": 7})
# daftar_nilai.append({"nama": "Tuti", "gender": "perempuan", "nilai": 8})
