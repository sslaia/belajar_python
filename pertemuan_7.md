# Belajar Bersama Python

Pertemuan 7, 4 September 2021


## Pengantar

Minggu lalu kita telah mengasah logika kondisi **while** dan **for** melalui pembuatan aplikasi [password.py](./latihan/password.py). Dengan contoh sederhana, kita telah menciptakan aplikasi password pintu yang jauh lebih _secure_ daripada yang dipakai di luar sana.

Harini kita akan meneruskan proses "mengasah" logika ini dengan membuat aplikasi **Fa'a**. Tetapi kalau ada waktu nanti kita maju selangkah dalam mengeksplorasi Python, yakni membuat fungsi atau _function_.

## Membuat aplikasi Fa'a

Apa instruksi untuk membuat aplikasi ini? Algoritma aplikasi ini hanya fantasi saya belaka dan tidak tahu bagaimana orang di Nias melakukan fa'a. Saya hanya berspekulasi saja.

Fa'a merupakan aplikasi yang digunakan untuk memprediksi prospek kecocokan satu pasangan. Untuk itu algoritma aplikasi membutuhkan data yang harus dimasukkan pengguna, yakni nama, umur dan jenjanga pendidikan.

Setiap komponen ini digunakan untuk menghitung poin tertentu. Aturannya adalah sbb.:

Untuk nama (hanya dibutuhkan nama depan, tidak masuk marga):
1. Bila nama keduanya mengandung huruf n, s atau t: 1 poin
2. Bila hanya salah satu nama: 2 poin
3. Bila tidak: 3 poin

Untuk umur:
1. Sama atau maksimum selisih 5 tahun: 3 poin
2. Selisih umur 5- 10 tahun: 2 poin
3. Selisih umur 10 tahun lebih: 1 poin

Untuk pendidikan:
1. Setara: 3 poin
2. Bila satu PT, yang lain SMA atau yang satu SMA, yang lain SMP: 2
3. Bila satu PT atau SMA yang lain SD: 1

Setelah itu semua nilai dijumlahkan dan berdasarkan angka total ini dibuat ranking yang ditampilkan dalam bentuk warna lampu lalu lintas:

1. Jumlah total = 3: menampakkan lampu merah
2. Jumlah total = 4-5: menampakkan lampu kuning
3. Jumlah total >= 6: menampakkan lampu hijau

Hasil akhirnya akan nampak dalam gambar berikut:

![Aplikasi Fa'a](./latihan/faa.png?raw=true)


## Langkah-langkah membuat aplikasi Fa'a

### Langkah 1: Mendefinisikan berbagai variable
```
nama_a = input("Tuliskan nama depan Anda (tanpa marga)\n")
nama_b = input("Tuliskan nama depan pasangan Anda (tanpa marga)\n")
umur_a = input("Tuliskan umur Anda (angka bulat tahun)\n")
umur_b = input("Tuliskan umur pasangan Anda (angka bulat tahun)\n")
pendidikan_a = input("Pendidikan terakhir Anda (SD: 1; SMP: 2; SMA: 3; PT: 4)\n")
pendidikan_b = input("Pendidikan terakhir pasangan Anda (SD: 1; SMP: 2; SMA: 3; PT: 4)\n")
huruf_khusus = ["n", "s", "t"]
```

### Langkah 2: Menghitung poin nama

Di bagian ini kita mengadakan perhitungan poin nama berdasarkan huruf yang terdapat dalam nama itu. Bila nama mengandung huruf n, s dan t poin menjadi 1, bila ketiga huruf itu tidak poin menjadi 3. 

Ketika menghitung poin sebagai pasangan, mereka mendapat 3 poin bila kedua nama tidak mengandung huruf kutukan di atas, 2 poin bila hanya salah satu nama dan 1 poin saja bila kedua nama mengandung huruf-huruf tsb. 

```
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
```

### Langkah 3: Menghitung poin umur

Yang dihitung di sini adalah jarak perbedaan umur. Bila selisih umur mereka antara 0 dan 5 tahun maka mereka mendapat 3 poin, bila antara 5 dan 10 dapat 2 poin, dan kalau lebih dari itu 1 poin saja.

```
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

```

### Langkah 1: Menghitung poin jenjang pendidikan

Algoritma di sini: pendidikan yang lebih setara memberi prospek yang lebih baik untuk pasangan. Pendidikan setara mendapat 3 poin, perbedaan setingkat 2 poin, lebih dari situ 1 poin.

```
# Menghitung poin pendidikan
#
# Membuat variable hasil perhitungan pendidikan
poin_pendidikan = 0

# Mengadakan kalkulasi
if int(pendidikan_a) == int(pendidikan_b):
    poin_pendidikan = 3
elif int(poin_nama_a) - int(pendidikan_b) == 1 or int(pendidikan_b) - int(pendidikan_a) == 1:
    poin_pendidikan = 2
else:
    poin_pendidikan = 1

# Menampilkan poin pendidikan
print(f"Poin dari pendidikan: {poin_pendidikan}")

```

### Langkah 1: Menghitung total poin pasangan dan menampilkannya

Ini gampang saja. Kita tinggal menambahkan semua poin dari masing-masing komponen dan menkonversinya ke dalam sistem lampu lalu lintas.

```
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


```

Selesai.


### Refleksi

Bagaimana seandainya komponen-komponen di atas (nama, umur, pendidikan) Anda ganti dengan menggunakan Facebook pengguna, menganalisa segala pos, bacaan, like, teman-teman dlsb.? Apakah Anda merasa hal ini fiksi atau nyata?


## Fungsi (_function_) di Python

Adalah praktek biasa memecah-mecah kode ke dalam bagian yang lebih kecil, yang berdiri sendiri. Selain membuat supaya kode lebih rapi, juga memungkinkan sehingga blok kode tertentu yang beberapa kali digunakan cukup sekali ditulis dan tak perlu ditulis ulang beberapa kali di mana blok tsb. dibutuhkan. Bagian ini disebut fungsi atau _function_ di Python.

Begini bagan sebuah fungsi:
```
def menghitung_harga_minyak():
    ...
    ...
    ...

## Program mulai dari sini
...
...

menghitung_harga_minyak()
..
..
menghitung_harga_minyak()
..
..
```

Seperti bisa dilihat dalam contoh di atas, setelah program mulai berjalan di dua tempat fungsi dengan nama `menghitung_harga_minyak()` dipanggil dua kali. Setiap kali fungsi tsb. dipanggil, program melompat ke tempat di mana fungsi tsb. didefinisikan. Setelah selesai, program kembali ke tempat semula.

Sebenarnya kita telah menggunakan beberapa fungsi, yang telah diikutkan secara _default_ dalam Python seperti fungsi `print()`. Fungsi print() tsb. berisi satu blok kode yang tak perlu kita tulis baris per baris. Kita cukup memanggil namanya dan memasukkan parameter dan argumen yang dibutuhkan, mis. "Harga minyak tanah di Pasar Gomo hari ini adalah: ", karena fungsi() memang didefinisikan untuk menerima satu string.

Selain fungsi _built-in_ ini kita bisa menciptakan sendiri fungsi yang kita butuhkan, mis.
```
# Fungsi poin_umur()
def poin_umur(umur_a, umur_b):
    selisih_umur = int(umur_a) - int(umur_b)
    print(f"Selisih umur: {abs(selisih_umur)}")
    
    if abs(selisih_umur) <= 5:
        poin_umur = 3
    elif abs(selisih_umur) <= 10:
        poin_umur = 2
    else:
        poin_umur = 1

    # Menampilkan poin umur
    print(f"Poin dari umur: {poin_umur}")
    
    # fungsi ini mengharapkan nilai balik, maka pakai kata kunci return
    return poin_umur
```


