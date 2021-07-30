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

boolean: `True` atau `False`

Contoh

```
print(4 < 3)
print(10 == 5)
print(6 > 5)
print(32 >= 32)
```

Cara mencek entah satu nilai `True` atau `False`

`bool("")`

Contoh

`print(bool("")`

Apa hasilnya? Coba pikir mengapa kira-kira hasilnya demikian?


## Lanjutan operasi logis (_logical operator_) yang berhubungan dengan nilai boolean

Kali lalu kita telah mengetahui `==, <, <=, >, >=` Hari ini kita tambah satu lagi dan sangat sering digunakan, yakni `!=`

Contoh

```
if ono_niha != orang_nias:
   print("Tenga ono niha sindruhu da'ö, he. Ha kece-kece.")
```


## Lanjutan pernyataan operasi logis (_logical operator conditional_)

Kita telah menggunakan `if` beberapa kali. Nah, erat berhubungan dan biasanya selalu tampil bersama dengan `if` adalah `else` dan `elif`

Contoh

```
if gae_sasoso < 100:
   print("Oi ataha na sa. Baloi mato ha'uga bongi awena ta'ohe ba fasa")
elif gae_sobou > 100:
   print("Talafo oya zobou. Lö mamawa gae ita migu andre.")
else:
   print("Lau be yaŵa ba moto. Mofanö ita ba fasa.")
```

operasi lainnya:

- `not` mis. `not` `ono_niha`, maka nilainya adalah `True` jika nilai `ono_niha` adalah `False` 
- `or` mis. `ono_manu` `or` `ono_mbawi`, maka nilainya adalah `True` kalau nilai salah satu entah `ono_manu` atau `ono_mbawi` nilainya `True`
- `and` mis. `ono_manu` `and` `ono_mbawi`, nilainya adalah `True` kalau keduanya `True`, kalau tidak salah satu nilainya beda maka hasilnya `False`


## Bagaimana mencek tipe data satu variable?

umur_pengguna = 37

`type(umur_pengguna)`

Contoh

`print(type(umur_pengguna))`

maka python akan menampilkan pesan bahwa umur-pengguna adalah tipe data `int`.


## Cara menulis pemisah ribuan: `_`

Contoh

`3_482` atau `4_200_000`


## Menghitung panjang satu string: `len()`

Contoh

`panjang_amaedola = len("Ligi-ligi siliŵi fa lö tofesu mbagi")`

`print(panjang_amaedola)` akan menampilkan angka 35, berarti ada 35 huruf dalam amaedola tsb.

Latihan:

`nama_kades = len(input("Hadia döi kepala desami? "))`

`print(nama_kades)` akan menampilkan jumlah huruf dalam nama kades ybs dan bukan nama kadesnya sendiri.


## Mencari tahu posisi dari satu karakter di dalam sebuah string

Menanyakan karakter tertentu dari sebuah string (str) digunakan tanda kurung siku (`[]`) dengan isi posisi karakter yang ingin kita cari. Misalnya menanyakan apa karakter pertama (posisi 0 dalam perhitungan komputer) dari string Ya'ahowu:

`print("Ya'ahowu"[0])`

Bagaimana saya menampilkan huruf `u`?


## Merevisi latihan-latihan yang telah dibuat

1. [print_1.py](./latihan/print_1.py) (latihan mencari kesalahan penulisan kode)
2. [print_2.py](./latihan/print_2.py) (mencari karakter dalam sebuah string panjang)
3. [bmi.py](./latihan/bmi.py) (menghitung indeks berat badan)
4. [bmi2.py](./latihan/bmi2.py) (bmi.py dengan kode yang lebih rapi)
5. [bagi_rata.py](./latihan/bagi_rata.py) (aplikasi buat keempat sahabat orang Nias di Jakarta)


## Membuat perhitungan tahun, bulan, hari dan jam sisa hidup

Bila ada waktu, kita akan membuat perhitungan ini.


