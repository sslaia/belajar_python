# Belajar Bersama Python

Pertemuan 9, 24 September 2021


## Pengantar

Minggu lalu kita telah berkenalan dengan apa yang dinamakan _function_ di Python, yakni sebuah mekanisme untuk membuat blok kode modular, artinya berupa blok-blok kecil, yang bisa digunakan berkali-kali dan di berbagai tempat, tanpa harus mengulangi menulis kode yang sama di semua tempat itu.

Setelah itu kita berkenalan dengan satu jenis daftar yang dinamakan _dictionary_, yakni satu daftar, yang item-item di dalamnya terdiri dari key-value pairs atau pasangan kunci-dan-nilai. Kita juga telah melihat bahwa _dictionary_ kita temukan dalam format json yang disebut obyek. Dan kita telah mendemonstrasikan bagaimana mengakses data dari Internet yang didapatkan dalam format json tsb.

Hari ini kita mendalami sedikit lebih jauh tentang function, yang telah kita mulai minggu lalu. Dan mudah-mudahan hal ini mempersiapkan kita memasuki topik baru nanti, yakni _class_, yang lebih kompleks dari _function_, tetapi juga jauh lebih menarik dari segi programming, walaupun untuk itu perlu juga keterangan teoretis yang kering.

Mari meneruskan eksplorasi kita tentang _function_ sambil juga mengulangi beberapa hal, sehingga kita lebih membatinkannya.

## Ada dua jenis _function_

Ya ada dua jenis _function_, yakni fungsi yang bawaan Python, artinya telah diikutsertakan di dalam Python dan fungsi yang didefinisikan oleh programmer.

Fungsi bawaan yang telah kita gunakan adalah print() dan input(). Namun yang akan sering nanti terdapat dalam berbagai kode yang kita tulis adalah fungsi yang kita ciptakan sendiri untuk mewujudkan maksud-maksud tertentu yang ingin kita capai.

Hal ini telah kita praktekkan minggu lalu pada contoh menghitung poin umur di aplikasi Fa'a.

## Ada dua tipe _function_

Kita juga telah melihat bahwa ada dua jenis _function_, yakni fungsi yang tak mengirim balik nilai, dan fungsi yang mengirim-balik nilai. Di Python kita tahu satu fungsi mengirim-balik satu nilai bila ada kata kunci _return_ di dalamnya.

Kata kunci yang sama juga digunakan di Dart/Flutter bila satu fungsi mengharapkan nilai balik, namun kalau tidak harus ditandai dengan kata kunci _void_.

## Function mempunyai dua jenis argumen

Satu fungsi mungkin kurang begitu bermanfaat bila sekedar menjalankan perintah dengan nilai yang selalu sama. Peranan fungsi justru baru menonjol bila fungsi tsb. menerima argumen yang bersifat dinamis dan memproses argumen tsb. untuk mendapatkan hasil.

Kita telah berkenalan dengan jenis argumen pertama, yakni sekedar memasukkan satu atau lebih argumen seperti dalam contoh berikut:
```
def salam_nias(gelar, salam):
    print("Ya'ahowu, ", gelar, ".", salam)
```
Lalu di salah satu tempat di dalam kode kita bisa memanggil fungsi bernama salam_nias ini dengan menyertakan argumen, mis.
```
salam_nias("Balugu", "Bologö dödöu. Lö afo-afoda.")
```
Perintah ini akan mencetak di layar
```
Ya'ahowu, Balugu. Bologö dödöu. Lö afo-afoda.
```
atau misalnya yang berikut ini
```
salam_nias("Nak", "Saya sudah lama menantikan kamu pulang.")
```
dan akan mencetak di layar
```
Ya'ahowu, Nak. Saya sudah lama menantikan kamu pulang..
```

Namun kalau diteliti lebih jauh, untuk bisa menjalankan fungsi ini, peng-input data harus tahu persis bahwa argumen pertama harus gelar dan argumen kedua harus salam. Jadi dia harus persis tahu posisi dari argumen tertentu di dalam fungsi. Dalam contoh ini, berarti pertama argumen gelar, lalu menyusul argumen salam. Karena itu argumen ini disebut _positional argument_, yakni argumen yang posisinya di dalam tanda kurung tsb. sangat menentukan.

Misalkanlah peng-input data agak mengantuk dan karena itu menulis fungsi ini sbb.
```
salam_nias("Lain kali saja datang lagi", "Sibaya") 
```
Maka kalau perintah ini dijalankan hasilnya menjadi
```
Ya'ahowu, Lain kali saja datang lagi. Sibaya
```

Nah untuk menghindari hal ini, apalagi kalau ke dalam fungsi itu kita menyertakan banyak argumen, maka ada jenis argumen yang kedua yang disebut argumen bernama atau _named argument_, yaitu satu argumen yang diberi nama, jadi seperti sebuah variable. Fungsi dengan argumen bernama mis. terlihat sbb.:
```
def bendera(negara = "Indonesia", warna = "merah putih"):
    print("Warna bendera ", negara, " adalah ", warna)
```
Maka kendati peng-input data menulis demikian
```
bendera(warna = "hijau putih merah", negara = "Italia")
```
Hasilnya akan tetap sama, menjadi
```
Warna bendera Italia adalah hijau putih merah
```
Cara penulisan fungsi seperti di atas juga disebut fungsi dengan nilai default, karena dalam fungsi sudah diberi nilai yang digunakan kalau tak ada nilai yang disertakan waktu fungsi dipanggil. Jadi kalau misalnya kita menjalankan fungsi ini sbb.:
```
bendera(negara = "Singapura")
```
maka akan menampilkan informasi yang salah berikut:
```
Warna bendera Singapura adalah merah putih
```

**Catatan:** Di sini nampak bahwa Python lebih fleksibel daripada Dart/Flutter. Kalau kita memanggil satu fungsi di Dart/Flutter dan hanya memasukkan satu argumen, padahal dalam definisinya mengharapkan dua, maka akan terjadi _error_.

## Fungsi dengan argumen sembarang

Ada skenario di mana kita tidak tahu berapa banyak argumen yang dibutuhkan. Nah, Python rupanya mengakomodasi kondisi semacam itu dengan menggunakan kata kunci args, yang didahului dengan tanda bintang (menjadi *args). Contoh
```
def salam(*args):
    for nama in args:
        print("Ya'ahowu", nama)
```
Lalu kita memanggil fungsi ini dengan argumen sembarang mis.
`salam("Anton", "Budi")` atau salam `salam("Anton", "Budi", "Tuti", "Kris", "Agung")`

Bukan hanya itu, mirip dengan argumen bernama di atas, di sini juga argumen bernama yang kita tidak tahu sebelumnya berapa jumlahnya, jadi digunakan kata kunci kwargs yang didahului dengan tanda bintang, menjadi *kwargs. kw itu merupakan singkatan dari key word, sama dengan argumen bernama atau berkata kunci.
```
def salam(*kwargs):
    for kunci in kwargs.keys():
        print("Kepada", key, ": Ya'ahowu", kwargs[key])
```
Lalu kita memanggil fungsi ini dengan argumen bernama sembarang mis.
```salam(bapak = "Anton", ibu = "Tuti", putra = "Budi", putri = "Kris")`
```
yang akan mencetak demikian di layar
```
Kepada bapak: Ya'ahowu Anton
Kepada ibu: Ya'ahowu Tuti
Kepada putra: Ya'ahowu Budi
Kepada putri: Ya'ahowu Kris
```

## Syarat-syarat menciptakan _function_ (rangkuman)

- Semua fungsi yang ada namanya didahului dengan kata kunci **def**
- Cara memberi nama fungsi adalah dengan menuliskannya dalam huruf kecil dan kalau terdiri dari dua kata atau lebih, keduanya dipisah dengan tanda garis bawah
- Satu fungsi bisa menerima beberapa argumen
- Baris judul fungsi ditutup dengan tanda titik dua, dan baris sesudahnya disebut badan fungsi
- Badan dari satu fungsi harus menjorok ke dalam sebanyak 4 spasi dari kiri



