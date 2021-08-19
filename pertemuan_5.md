# Belajar Bersama Python

Pertemuan 4, 20 Agustus 2021


## Pengantar

Pada pertemuan terakhir (pertemuan 4) kita telah melatih penggunaan **elif** dan *nested if* (kondisi if yang memiliki kondisi bawahan lagi).

Kemudian kita juga berkenalan dengan *list* (mendeklarasikan satu variable menjadi satu daftar) dan bagaimana mengakses item di dalam daftar tsb. yang sangat mirip dengan cara mengakses huruf di dalam satu string.

Hari ini kita berkenalan fungsi tambahan yang bisa digunakan untuk memanipulasi entah isi dari satu *string* atau berbagai item di dalam satu *list*.

Kemudian kita introduksi topik baru yang disebut pengulangan atau dalam bahasa Inggris *iteration* atau *loop* Fungsi seperti ini akan sangat sering digunakan, misalnya kita mau menyebut satu per satu item di dalam satu daftar. Tetapi bisa juga mengulang-ulang operasi tertentu sampai satu kondisi terpenuhi mis.


## Manipulasi list: lanjutan



## Mengenal operasi pengulangan *iteration/loop*

Operasi pengulangan terdapat di berbagai bahasa pemrograman. Di dalam python ada dua jenis pengulangan yakni **while** dan **for**

### Pengulangan **while**

Pengungalangan menggunakan kondisi **while** biasa digunakan kalau jumlah pengulangan tsb. *tidak diketahui* dan karena itu blok kode tertentu diulang-ulang terus sampai nilai tertentu didapatkan.

```
jumlah_telur = input("Masukkan jumlah telur: ")
hitung = 1
while hitung <= int(jumlah_telur):
    print(f"Masukkan telur no {hitung} ke dalam panci!")
    hitung += 1
print("Ha da'ö fefu gadulo!")
```

Untuk melihat hal ini dalam aksi, coba simpan kode tsb. dalam satu berkas puthon dan jalankan.


### Pengulangan **for**

Pengulangan ini sama dengan yang sebelumnya di atas, hanya jumlah pengulangannya telah diketahui. Biasanya pengulangan **for** digunakan untuk jarak (*range*) antara dua angka atau antara dua item di dalam satu daftar. Contoh
```
for x in range(0, 10):
    print(x, ' ', end='')
print("\nSelesai")
```

Untuk melihat hal ini dalam aksi, coba simpan kode tsb. dalam satu berkas puthon dan jalankan.

Kalau diamati pengulangan **while** dan **for** sangat mirip. Tetapi ada perbedaan penting. Dalam pengulangan **for**:
- tak perlu lagi menghitung jumlah pengulangan 
- digunakan untuk **range** dan angka terakhir seperti dalam 10 dalam range(0, 10) tidak ikut dihitung
- tak perlu membuat variable seperti di while

**argumen ketiga range**

Yang menarik range bisa memungkinkan yang namanya argumen ketiga (third argument) mis. range(0, 10, 3) yang berarti buat operasi di bawah ini dalam range 0 sampai 10 tetapi lompat-lompat 3. Dengan menggunakan kode sebelumnya:
```
for i in range(0, 10, 3):
    print(i, ' ', end='')
print("\nSelesai")
```
maka yang akan dicetak adalah 0  3  6  9! 

**menggunakan yang dinamakan wild card _**

Pengulangan for mengenal penggunaan yang dinamakan wild card (_) untuk satu pengulangan yang tidak membutuhkan penggunaan nilai hasil, mis. dalam pengulangan berikut
```
for _ in range(0, 10):
    print('*', end='')
print()
```
kode ini hanya akan mencetak tanda * di layar, jadi tidak perlu tahu entah nilainya 1, 2 atau 3 dst. Tentu saja **_** itu adalah variable juga, namun dalam bahasa pemrograman hal ini disebut variable anonim. Akan ada skenario tertentu yang membuat penggunaan hal ini lebih tepat daripada penggunaan variable biasa.

**Catatan tentang penamaan variable i dalam pengulangan**

Kali lalu kita belajar bahwa kita harus memberi nama variable yang bermakna, artinya yang memungkinkan kita mengetahui apa dan untuk apa variable tsb. mis. dalam contoh di atas `jumlah_telur`. 

Kita tahu bahwa memberi nama variable seperti x atau z atau a atau c dlsb. tidak dianjurkan kendati bukan masalah menggunakannya.

Namun ada kekecualian dalam nama variable untuk pengulangan (*loop*). Telah menjadi praktek umum untuk menggunakan variable **i**, **j**, dst. seperti bisa dilihat dalam potongan kode *range* di atas. Itu berarti kalau lain kali Anda menemukan satu potongan kode dan nama variablenya adalah i, j dst. maka Anda otomatis tahu bahwa blok kode tsb. hampir 100% merupakan sebuah *loop*.

**Menghentikan satu pengulangan: break**

Sering dalam satu pengulangan dibutuhkan penghentian kalau kondisi tertentu terpenuhi, mis. perintah: 

```
mau_hujan = "t"

while mau_hujan == "t":
    print("Jemur pakaian di luar!")
    if mau_hujan == "y":
       break
    mau_hujan = input("Apakah mau hujan? (y / t) ")    
print("Besok saja menjemur pakaian!")
```

Sesuai dengan prinsip *loop* kode ini akan berjalan terus sampai suatu ketika pengguna menjawab ya. Katakanlah kode di atas merupakan potongan kode untuk satu robot, yang diciptakan oleh anak-anak dari Nias. Setiap kali robot bertanya kepada pengguna, apakah hari ini hujan atau tidak. Selama jawaban yang diterima adalah t (tidak) maka robot tsb. akan menjemur pakaian di luar.

Program robot semacam ini bisa ditingkatkan lagi dengan mengirim pertanyaan tsb. ke Badan Metereologi,Klimatologi dan Geofisika, yang menyediakan data terbuka di data.bmkg.go.id/prakiraan-cuaca/ Mudah-mudahan di masa depan kita bisa membuat aplikasi dengan menggunakan data dari sana!


## Skenario di mana pengulangan digunakan

Menurut Anda hal-hal apa saja yang di dalamnya ada pengulangan dan karena itu kita bisa menerapkan *loop* waktu menerjemahkannya ke dalam kode python?

Apakah Anda pernah melihat hal ini di pintu masuk satu pertunjukkan, Gereja, kapal di pelabuhan dslb?

Apakah menurut Anda roda mobil Anda menganut prinsip *loop*? Bisakah Anda membayangkan bagaimana kodenya?

Bagaimana dengan daftar lagu atau video untuk diputar (*playlist*) di YouTube? Bagaimana menurut Anda permainan dadu? Adakah *game* yang Anda kenal yang kemungkinan besar di belakangnya adalah *loop*?

Apakah kode program di belakang pencarian yang kita lakukan di Google juga menggunakan *loop*? Bisakah Anda membayangkan kira-kira bagaimana?


## Membuat game main dadu

Kalau ada waktu kita diskusikan bagaimana membuat *game* main dadu yang sederhana untuk menerapkan apa yang telah kita pelajari tentang *loop* dalam hidup nyata.

