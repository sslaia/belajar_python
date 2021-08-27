# Belajar Bersama Python

Pertemuan 6, 28 Agustus 2021


## Pengantar

Pada pertemuan terakhir (pertemuan 5) kita telah melatih penggunaan *loop* (**while** dan **if**) melalui pembuatan aplikasi dadu. Kita juga telah membahas lebih lanjut berbagai metode manipulasi daftar (*list*).

Saya janji minggu lalu kita akan masuk ke topik baru yakni membuat fungsi **def**, namun saya pikir baiklah pertemuan kali ini kita gunakan untuk lebih mengasah *logika* programming kita dalam penggunaan *loop* yang sering sekali digunakan dalam setiap aplikasi/program.

Saya pikir akan menjadi terlalu sulit bagi kita nanti kalau kita langsung melompat ke fungsi **def** yang sudah lebih kompleks, bila belum menguasai berbagai perkakas dasar yang kita butuhkan


## Membuat aplikasi password di pintu gudang emas

Dalam tugas ini kita membuat satu program/aplikasi password pintu masuk gedung. Bayangkan tugasnya demikian:

Anda diminta membuat program password pintu masuk gudang emas satu bank. Tamu harus memasukkan password di layar terminal di pintu dengan menerka huruf dari password. Lihat gambar berikut:

![Program Password Pintu](./latihan/password.jpg?raw=true)

1. Password terdiri dari lima kata berikut: jujur, setia, santun, hormat, ceria. Dan setiap kali diacak.

2. Sebagai alat bantu di layar akan ditampilkan berapa huruf dalam kata password tsb.

3. Pertama tamu diberi kesempatan mencoba-coba terus sampai dia menemukan satu kata dari password saat itu.

4. Setelah itu dia hanya diberi kesempatan memasukkan huruf sebanyak jumlah huruf dalam kata password tsb.

5. Kalau dia berhasil menerka semua huruf dalam password, pintu akan dibuka dan dia bisa mengambil emas sebanyak mungkin dari gudang.

6. Kalau dia gagal, maka dia mendapat pesan terminal bahwa dia tidak mendapat otorisasi dan bisa mencoba lagi setelah 24 jam!


**Hal-hal apa yang kita butuhkan?**

Pertama: kita butuh daftar (*list*) karena password terdiri beberapa kata yang setiap kali diacak (no. 1).

Kedua: untuk memungkinkan pengacakan, kita harus menggunakan modul random. Silakan memasukkan baris kode ini di baris paling atas berkas kode: `import random`

Ketiga: kita perlu membuat beberapa variable, yang memungkinkan kita menampilkan di layar berapa huruf password tsb., kemudian kata apa yang menjadi password setelah diacak, dan jumlah huruf dalam password yang aktual.

Keempat: kita perlu menemukan cara menampakkan di layar berapa huruf dalam kata password tsb. tetapi dengan mengganti huruf-hurufnya dengan tanda **_** (no. 2).

Kelima: Kita perlu memikirkan baik-baik bagaimana kita memungkinkan pengguna memasukkan huruf sampai salah satu huruf dari password ditemukan, sebelum *count down* mulai (no. 3).

Keenam: Seperti yang sebelumnya kita akan menggunakan *loop* **while** dan **for** untuk memberi kemungkinan kepada pengguna memasukkan huruf terkaan, yang setiap kali kita periksa entah berpadanan dengan salah satu huruf dalam password.


**Menerjemahkan hal-hal ini ke dalam kode python**


