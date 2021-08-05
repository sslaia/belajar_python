# Belajar Bersama Python

Pertemuan 4, 6 Agustus 2021


## Pengantar

Minggu lalu kita tidak sempat membuat aplikasi kalender menghitung sisa hari-hari kita. Saya harap kita bisa melakukannya di akhir sesi hari ini.

Namun supaya kita lebiih yakin diri dengan apa yang telah kita pelajari (kata orang Inggris menjadi *proficient*), dan itu hanya bisa tercapai melalui praktek menulis kode lagi dan lagi, maka kita berusaha menerapkan apa yang telah kita pelajari atas kode-kode yang telah kita tulis di masa lalu.

Dengan demikian kita juga mengetahui bagaimana kita menyempurnakan kode kita berdasarkan level pengetahuan yang sedang kita jalani.

Jadi kita akan menyempurnakan kode aplikasi menghitung indeks berat badan ideal (bmi.py) dan menerapkan persyaratan **elif**, yang baru kita pelajari minggu lalu, di dalamnya.

Kita juga akan menambah satu kemungkinan baru yang dinamakan **nested if**, artinya persyaratan yang memiliki satu persyaratan bawahan atau malah lebih dari satu.

Setelah itu kita berkenalan dengan topik baru hari ini, yakni *list*. Itu adalah satu tipe data python yang isinya merupakan daftar dan bukan sekedar rangkaian huruf seperti string atau angka seperti integer/float.


## Memperbaiki kode bmi.py menggunakan elif dan else

Minggu lalu kita belajar perintah persyaratan (*conditional*) tambahan terhadap **if** yakni **elif**. Hari ini kita memperbaiki kode [bmi.py](./latihan/bmi.py) yang kita buat kali lalu dengan menggunakan pengetahuan kita yang baru. Kali lalu kita membuatnya dengan pengetahuan yang terbatas, karena itu kode tsb. tidaklah elegan.

Bukalah kode [bmi.py](./latihan/bmi.py) dan mari mengatamatinya bersama-sama. Perhatikan blok kode yang ada persyaratan **if**.

Apakah yang terjadi di situ? Ternyata kita membuat 3 kali persyaratan **if**. Ini tentu saja *tidak salah*, tetapi juga *tidak efisien*. Itu berarti bahwa python/komputer akan menjalankan semua baris-baris kode tsb. satu per satu dari atas sampai ke bawah.

Kita bisa membuat kode tsb. lebih efisien dengan membuat segala operasi persyaratan ini menjadi satu blok kode. Artinya python/komputer tak perlu menjalankan semua persyaratan itu, melainkan berjalan mulai dari atas dan secepat satu syarat terpenuhi dia berhenti dan melompat keluar dari blok kode. 

Marilah mengubah kode tsb. dengan menjadikan keseluruhan blok tsb. satu persyaratan **if**, sedangkan yang lain hanyalah merupakan bagian dari **if** tsb. dengan menggunakan **elif** dan **else**

Selamat! Anda telah menjadi *advanced coder*!


## *Nested if*

Dalam hidup nyata, sering terjadi bahwa satu syarat diikuti oleh syarat bawahan. Perhatikan misalnya dialog berikut.

Budi merengek-rengek kepada Bu Tuti, mamanya, ingin makan es krim. Mamanya mengatakan, "Budi, tidak sehat makan es krim terlalu sering, karena di dalamnya banyak gula. Oleh karena itu, kamu boleh makan es krim sekali seminggu, kecuali kalau ada tamu di rumah dan tamu disuguhi es krim."

Nah sekarang Bu Tuti datang kepada Anda untuk membantu dia membuat satu aplikasi yang menolong mencek entah Budi boleh makan es krim atau tidak. Cobalah sekarang menerjemahkan dialog tsb. ke dalam satu blok kode python. Bagaimana caranya?

Tentu saja pertama kita perlu mencek entah Budi telah makan es krim minggu ini (jawaban **y**) atau belum (**t**). Kalau belum (**t**), maka komputer langsung melompat ke pernyataan else yang sejajar if tsb, artinya memberitahu Budi bahwa dia *boleh* makan es hari ini.

Namun kita tahu pula bahwa, walaupun Budi telah makan es krim minggu ini, kalau hari itu ada tamu di rumah dan kebetulan tamu mendapat es krim, maka Budi boleh juga makan es krim. Kalau syarat ini tidak terpenuhi, Budi tidak boleh makan es krim hari ini. Inilah yang disebut **nested if** artinya ada pernyataan kondisional bawahannya.

Untuk program ini kita membutuhkan dua variable yang nilainya harus diminta dari pengguna aplikasi, yakni `telah_makan_es_krim_minggu_ini` dan `tamu_dapat_es_krim`. Blok kodenya bisa seperti ini:

```
# mulai dengan meminta input dari pengguna
telah_makan_es_krim_minggu_ini = input("Apakah kamu telah makan es krim minggu ini? Tulis y atau t: ")

# persyaratan utama if mulai

if telah_makan_es_krim_minggu_ini == "y":

    # kendati Budi telah makan es krim (jawaban y), 
    # ada kondisi lain yang memungkinkan dia bisa makan es krim
    # karena itu kini menyusul persyaratan bawahan
    # dan mulai dengan menanyakan Budi
    # apakah hari ini ada tamu dan apakah tamu tsb. mendapat es krim

    tamu_dapat_es_krim = input("Apakah saat ini tamu ditawari es krim? Tulis Y atau T: ")

    if tamu_dapat_es_krim == "y":
        print("Selamat, Budi. Hari ini kamu boleh makan es krim!")

    # kalau tamu tidak mendapat es krim (jawaban **t**), 
    # maka Budi mendapat pesan bahwa dia tidak boleh makan es krim

    else:
        print("Maaf, Budi. Jatahmu untuk minggu ini telah terpenuhi. tunggu sampai minggu depan yah!")

# kalau jawaban adalah **t** (tidak),
# maka Budi mendapat pesan bahwa dia boleh makan es krim

else:
    print("Selamat, Budi. Hari ini kamu boleh makan es krim!")
```

Pertanyaan:
1. Coba pikirkan sekali lagi logika program tsb. Apakah ada cara lain mengungkapkan persyaratan ini? Bagaimana seandainya yang akan di-tes menjadi True/False adalah jawaban **t**? Apa akibatnya bila menggunakan alur logis seperti ini? Coba bereksperimen dengan kemungkinan jawaban yang ada (**y** dan **t**) untuk mengetahui hal ini.
2. Contoh **nested if** dalam aplikasi es krim di atas hanya satu contoh. Adakah contoh lain yang Anda pikir menuntut adanya **nested if** ini?


## Lanjutan tipe data python: *list*

Selain int/float dan str ada juga tipe data python bernama list. Ngomong-ngomong, saya baru menemukan satu website programming yang telah meringkas berbagai perintah python, yakni [w3schools.com](https://www.w3schools.com/python/python_lists.asp) Dan sesuai dengan prinsip kita, tak perlu menemukan kembali roda pedati, baiklah kita menggunakan ringkasan dari situs tsb.

Contoh:

```
hewan_khas_nias = ["beo", "sökha", "manu ndru'u"]
```

Dan seperti kita pelajari minggu lalu, kita bisa menampilkan setiap huruf dalam satu string dengan mengakses langsung posisinya dalam string tsb. mis. `"Ya'ahowu"[2]`, demikian juga kita bisa mengakses setiap item dalam *list* dengan menggunakan pola yang sama. Misalnya dalam contoh di atas `print(hewan_khas_nias[2])` akan menampilkan item di posisi ke-3!

Operasi sperti ini sangatlah berguna. Misalkan kita mau men-*scan* daftar isi satu buku, maka kita bisa menulis kode python: 

```
daftar_isi = ["Pengantar", "Bab 1. Hewan piaraan utama di Pulau Nias", "Bab 2. Kedudukan babi dalam budaya Nias"]
```

Kemudian kalau kita ingin mengakses salah satu item dalam daftar isi tsb. dan menampilkannya di layar, maka kita tinggal menulis kode `print(daftar_isi[2])`

Demikian juga kita bisa menerapkan `len()` yang kita pelajari minggu lalu untuk *list*. Jadi untuk mengetahui berapa banyak item dalam list `daftar_isi` kita tinggal mengapitnya dengan `len` menjadi `len(daftar_isi)`

Pertanyaan:
1. Apakah ada hal-hal lain yang Anda pikir menggunakan *list* seperti ini?
2. Apakah item di dalam *list* tsb. hanya berupa *str (string)* atau bisa juga merupakan angka seperti *int (integer)* atau *float*?
3. Cobalah menerka entah item di dalam *list* tsb. bisa sama alias berulang mis. `lagu_favorit = ["He akhi", "Ngenu-ngenu dödö", "He akhi?"]`? Bagaimana dengan daftar nilai dalam ijazah misalnya?


## Bersama mendesign aplikasi Hari Hidupku

Minggu lalu, kita belum sempat membuat aplikasi kalender, yang menghitung tahun, bulan, hari sisa hidup kita.

Dalam pertemuan ini kita membahas hal ini, bersama-sama kita terapkan pengetahuan yang telah kita dapatkan untuk membuat aplikasi tsb.

Hari ini kita membuat versi 1.0 dari aplikasi kita.
Dalam kesempatan berikut kita bisa mengembangkannya menjadi versi 2.0 dengan menambah berbagai fitur.

