# Belajar Bersama Python

Pertemuan 2, 24 Juli 2021


## Pengantar

Merangkum apa yang telah dipelajar kali lalu, tentang operator aritmatika dan hirarkinya.

- Tanda kurung (parentheses): ()
- Pangkat (exponential): **
- Pengalian (*) dan pembagian (/)
- Penambahan (+) dan pengurangan (-)

Kalau misalnya dalam satu perhitungan di mana dimulai dengan penambahan dan pengurangan dan diikuti dengan pembagian atau pengalian, maka supaya penambahan dan pengurangan dijalankan lebih dulu tempatkan penambahan dan pengurangan tsb. di dalam tanda kurung mis. `(3 + 2) / 2 * 3`. Kalau tanda kurung tidak ada, maka yang dikalkulasi duluan adalah 2/2 lalu 1 * 3 baru 3 + 3.

Hari ini kita meneruskan dengan operator lainnya, lalu kita teruskan dengan hal-hal dasar yang perlu diketahui dalam menulis kode program python.


## Operator aritmetika python (lanjutan)

- `//`: mengambil nilai dasar, mis. `7 / 3 = 2.333`, maka hasilnya adalah 2. Artinya semua angka di belakang titik dibuang 2.91235 pun hasilnya 2.
- `%` : sisa (remaining), mis. `5 % 2 = 1`, karena 2 * 2 = 4, tetapi `6 % 2 = 0`, karena 3 * 2 = 6.
- `**`: pangkat, mis. `2 ** 2 = 4`, `2 ** 3 = 8`, `2 ** 4 = 16`


## Operasi lainnya:

- `==`: sama dengan
- `<` : kecil dari
- `<=`: kecil atau sama dengan
- `>` : besar dari
- `>=`: besar atau sama dengan
- `+=`: menambahkan nilai di sebelah kanan ke variable sebelah kiri dan menjadikannya sebagai nilai variable yang baru mis. `böli_gadao = 15000`. Kalau kita menulis `böli_gadao += 10000` maka hal itu sama dengan menulis `böli_gadao = böli_gadao + 10000`
- `-=`: mirip dengan di atas
- `*=`: mirip dengan di atas
- `/=`: mirip dengan di atas


## Tipe data (_data type_)

- `int`   : integer, yakni angka bulat
- `float` : angka pecah (mis. 5.6739)
- `str`   : string, yakni rangkaian huruf


## Menampilkan sesuatu di layar: `print()`

`print` adalah perintah dasar python untuk menuliskan di layar apa yang ada yang dalam tanda kurung. Mis. untuk menampilkan kalimat berikut, maka penulisannya adalah

`print(“Ya’ahowu banuada”)`

Yang akan dilihat pengguna aplikasi adalah:

`Ya’ahowu banuada` 

atau

`print(5 + 3)` akan menampilkan di layar:

`8`

Aturan penggunaan perintah `print`:
- Kalau mau menampilkan kalimat, maka kalimat tsb. harus diapit dengan tanda kutip (`"`).
- Kalau mau "menyambung" dua kata/atau kalimat, gunakan tanda `+`, mis. `print("Na lö inötö ma’ökhö " + "ba mahemolu tola göi")`
- Kalau mau membuat garis baru sisipkan tanda `\n` mis. `print("Lau ndrege da’ö ua!\nMahemolu owulo ita zui")`
- Kalau menampilkan angka untuk operasi aritmatika, maka angka-angka tsb. tidak diapit tanda kutip


## Meminta pengguna mengetik di layar: `input`

Contoh:

`input("Ha’uga mböli wanikha sami ba Gunungsitoli? ")`


## Menyimpan nilai hasil (_variable_)

Untuk menyimpan satu nilai kita menggunakan yang namanya variable. Variable itu harus menggunakan nama, satu huruf mis. `x` atau merupakan satu kata yang lebih jelas mis. `böli_wanikha`

Contoh:

`böli_wanikha = input("Ha'uga mböli wanikha sami ba Gusit? ")`

`print(böli_wanikha)`


## Menulis keterangan (comment): `#` atau `'''`

Contoh

```
# di bawah ini adalah perhitungan utang
# setiap petani, setelah mereka menerima
# semua mesin yang dibeli di Medan

(jumlah_peserta * harga_per_mesin + (12 * (jumlah_peserta * harga_per_mesin) / 100) + biaya_perjalanan) / jumlah_peserta
```

Alternatif lain untuk menulis keterangan adalah dengan mengapitnya dengan tanda petik tiga, terutama untuk keterangan yang panjang

```
'''
Kalau keterangan lebih dari satu baris
atau bahkan panjang lagi
kadang lebih nyaman memasukkannya
dalam tanda petik tiga
'''
```

Keterangan sangat penting dalam satu aplikasi. Bukan hanya membuat orang lain dapat mengerti apa tujuan bagian kode tertentu, melainkan juga untuk membuat diri sendiri mengerti blok kode tsb. di masa depan. Misalnya dalam contoh rumus di atas. Tanpa keterangan, kita tidak tahu rumus apa itu.


## Siap mengkalkulasi indeks berat badan ideal?

Menjalankan program [bmi.py](./latihan/bmi.py) di python command prompt dan dalam **Visual Studio Code**! Caranya? Buka [bmi.py](./latihan/bmi.py), kopi isinya dan simpan dengan nama bmi.py di komputer Anda. Kemudian di **Command Prompt** ketik perintah berikut di folder di mana berkas bmi.py telah disimpan:

`python bmi.py`

Selamat menjalankan program pertama python!
