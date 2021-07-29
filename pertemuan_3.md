# Belajar Bersama Python

Pertemuan 3, 30 Juli 2021


## Merangkum kembali apa yang telah dipelajari sampai sekarang

- Hirarki operasi aritmatika. Coba hitung berapa 3 * 3 + 3 / 3 - 3? Coba cari cara supaya hasilnya 3!
- Jenis-jenis operasi aritmatika lainnya
- Tipe data (_data type_): int, float, str
- Konversi (_type casting_) antara berbagai tipe data, mis. `int("3")`, atau `str(427)`, atau `float(böli_gadao)`
- Kalau ingin membuat desimal gunakan `round(variable, 2)` atau yang kemungkinan yang lebih baik yang akan diterangkan di bawah
- Aturan perintah `print` termasuk tanda untuk memungkinkan penyisipan nilai variable dalam satu string, yakni `f`
- Perintah `input` untuk menanyakan masukan dari pengguna program
- Menyisipkan keterangan/catatan dalam kode dengan menggunakan tanda `#` untuk komentar satu baris dan tanda `'''` untuk komentar lebih dari satu baris.


## Lanjutan tipe data python (_data type_)

- boolean: True atau False


## Bagaimana mencek tipe data satu variable?

umur_pengguna = 37

`(type(umur_pengguna))`

Contoh

`print(type(umur_pengguna))`

maka python akan menampilkan pesan bahwa umur-pengguna adalah tipe data int.


## Menampilkan nilai desimal

Selain cara round(nama_variable, 2) ada cara yang lebih tepat untuk menampilkan angka desimal- 


## Cara menulis pemisah ribuan: `_`

Contoh

`3_482`


## Menghitung panjang satu string: `len()`

Contoh

`panjang_amaedola = len("Ligi-ligi siliŵi fa lö tofesu mbagi")`

`print(panjang_amaedola)` akan menampilkan angka 35, berarti ada 35 huruf dalam amaedola tsb.

Latihan:

`nama_kades = len(input("Hadia döi kepala desami? "))`

print(nama_kades)


## Mencari tahu posisi dari satu karakter di dalam sebuah string

Contoh

`print("Ya'ahowu"[0])`

Bagaimana saya menampilkan huruf `u`?


## Merevisi latihan-latihan yang telah dibuat

1. Lima petani
2. bmi.py
3. Empat sahabat


## Membuat perhitungan tahun, bulan, hari dan jam sisa hidup


