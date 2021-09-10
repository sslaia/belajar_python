# Belajar Bersama Python

Pertemuan 8, 10 September 2021


## Pengantar

Minggu lalu kita membuat sebuah aplikasi sederhana bernama [Fa'a](./latihan/faa.py). Dan bersama dengan aplikasi [Password](./latihan/password.py) kita telah mengasah logika melalui berbagai kondisi **if** serta penggunaan pengulangan **while** dan **for**.

Hari ini pada bagian pertama kita berkenalan dengan topik baru yang disebut _function_ (fungsi). Kita telah menggunakannya beberapa kali baik di Flutter maupun di Python, tetapi kita tidak begitu menyadarinya.

Kemudian pada bagian kedua kita maju selangkah dalam pengetahuan kita tentang daftar. Hari ini kita akan berkenalan dengan satu daftar istimewa yang disebut _dictionary_ (kamus).

Tapi mari mulai dengan fungsi atau dalam bahasa Inggrisnya _function_.


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

Sebenarnya kita telah menggunakan beberapa fungsi, yang telah diikutkan secara _default_ dalam Python seperti fungsi `print()`. Fungsi `print()` tsb. berisi satu blok kode yang tak perlu kita tulis baris per baris lagi. Kita cukup memanggil namanya `print()` dan memasukkan kata atau kalimat, yang kita ingin cetak, menjadi argumen dari fungsi ini ke dalam tanda kurung di belakangnya.

Namun yang lebih menggairahkan lagi adalah bahwa selain berbagai fungsi _built-in_ yang telah disediakan Python, kita bisa menciptakan sendiri fungsi yang kita butuhkan. Lihat mis. fungsi berikut yang dibuat berdasarkan kode aplikasi **Fa'a** yang kita buat minggu lalu:

```
# Fungsi menghitung_poin_umur()
def menghitung_poin_umur(umur_a, umur_b):
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
Seperti bisa dilihat, semua baris kodenya sama, kecuali baris pertama (`def menghitung_poin_umur`) dan baris terakhir (`return poin_umur`)

Barangkali menarik diperhatikan bahwa kendati namanya fungsi, kata kunci yang dipakai adalah **def**. Anatominya adalah mulai dengan kata kunci **def** menyusul **nama_fungsi** dengan tanda kurung **()** untuk memasukkan argumen. Jadi dalam contoh di atas: `def menghitung_poin_umur(umur_a, umur_b):`

Misalkan kita menulis kode program satu robot, yang bertugas menjemur pakaian setiap pagi. Satu fungsi yang selalu berulang dilakukan robot adalah mencek data terakhir cuaca di website Badan Meteorologi, Klimatologi dan Geofisika, sekali setiap 6 jam. Blok kode untuk itu bisa dibuat dalam satu fungsi mis. `cek_bmkg` dan pada saat dibutuhkan, robot tinggal memanggil fungsi tsb.

Di pabrik terdapat banyak hal yang sama yang terus-menerus berulang dijalankan oleh mesin. Kode program mesin tsb. pasti banyak menggunakan fungsi. Kali lalu kita membuat aplikasi password. Keseluruhan aplikasi itu bisa menjadi satu fungsi, yang senantiasa dipanggil kalau ada orang yang mau membuka pintu.

**Perhatian:** Mereka yang belajar Flutter telah mengenal berbagai fungsi seperti ini. Di python tidak begitu jelas tipe data fungsi, contohnya berikut ini:
```
def salam_nias(nama):
    print(f"Ya'ahowu, {nama}")
    
def uang_rokok(jumlah_kontrak):
    jumlah_kontrak * 0.20
```
Fungsi pertama (`salam_nias`) tidak mengirim-balik hasil, sedangkan yang kedua (`uang_rokok`) mengirim-balik hasil kalkulasi `20% * jumlah_kontrak` yang bisa kita simpan dalam satu variable. Bila kita melakukan hal yang sama dengan fungsi `salam_nias` kita akan mendapatkan _error_.

Di Flutter kita harus menandai entah satu fungsi mengirim-balik satu nilai atau tidak. Fungsi yang tidak mengirim-balik nilai ditandai dengan void, seperti fungsi berikut dari aplikasi [Burung Nias](https://github.com/sslaia/burung_nias/blob/pertemuan-7/lib/main.dart)
```
  void _sembarangBurung() {
    setState(() {
      _counter = Random().nextInt(9) + 1;
      _burungPilihan = _burungNias[_counter];
    });
  }
```
Sedangkan contoh fungsi, yang mengharapkan nilai balik, kita lihat dalam aplikasi [Gogowaya](https://github.com/sslaia/gogowaya/blob/main/lib/main.dart) kemarin. Yang diharapkan balik adalah `List<Photo>`:
```
List<Photo> parsePhotos(String responseBody) {
  final parsed = jsonDecode(responseBody).cast<Map<String, dynamic>>();

  return parsed.map<Photo>((json) => Photo.fromJson(json)).toList();
}
```

## Refleksi

Coba bayangkan skenario apa saja yang membutuhkan pembuatan fungsi.


## Mengenal daftar yang dinamakan _dictionary_ (kamus)

Sampai sekarang kita telah mengenal yang dinamakan daftar. Dan kita tahu cara membuat daftar adalah dengan mendefinisikan satu variable lalu mengapit semua item di dalam daftar dengan tanda kurung siku seperti berikut:
```
burung_nias = ["Beo", "Buru'u", "Magio", "Nagoyomanase", "Towi-towi", "Nazese", "Gogowaya", "Miti-miti", "Siliŵi", "Boroa"]
```

Tetapi dalam hidup nyata ada banyak hal yang tidak bisa direkam dalam daftar sederhana semacam ini. Salah satunya adalah entri dalam kamus (dan mungkin karena itu nama daftar semacam ini disebut _dictionary_). Contohnya adalah sbb:
```
nias_wiktionary = {
 "fole": "Naha wanutu afo khö ndra satua si lö ifö ba boha", 
 "farate": "Naha wemörö ni'alaŵa'ö nifazökhi moroi ba geu ma zui ba zi'öli",
 "aurifö": "Sauri ba danö he urifö ba he göi sauri tanö bö'ö."
}
```
Ciri khas dari daftar semacam ini adalah adanya yang dinamakan key-value pairs (pasangan kunci-nilai). Dari contoh di atas kita melihat bahwa entri kamus menjadi kunci, sedangkan definisi kata menjadi nilainya.

Mereka yang kemarin belajar JSON pasti langsung mengenali kembali cara penulisan seperti ini, yang sangat mirip dengan cara penulisan obyek json. Hanya di sini di Python namanya dictionary.

Nah bagaimana mengakses item di dalam satu kamus? Kita telah tahu kita bisa mengakses satu item dalam satu daftar sbb: `nias_wiktionary[0]`. Tetapi hal ini justru menghasilkan error di dalam sebuah kamus.

Singkatnya dalam kamus tak ada indeks 0, 1, 2, dst. Yang ada adalah kunci atau key. Jadi untuk mengakses item di dalam kamus harus menyebutkan kuncinya. Jadi misalnya kalau saya ingin mengakses item yang pertama dalam `nias_wiktionary` di atas, saya harus menulis `nias_wiktionary["fole"]`.

Konsekuensinya? Kita harus tahu nama kuncinya untuk bisa mengakses isinya. Dan nama kunci tsb. harus ditulis persis seperti tertulis, kalau tidak program akan mengeluarkan error.

## Kamus di dalam kamus

Pada kenyataannya berbagai daftar yang kita temui merupakan kamus di dalam kamus. Contohnya adalah sbb.:
```
Daftar biasa:
kabupaten_kota = ["Nias", "Nias Utara", "Nias Barat", "Nias Selatan", "Gunungsitoli"]

Daftar berupa kamus:
kabupaten_kota = {
 "Nias": "Ibu kotanya Gidö"
 "Nias Utara": "Ibu kotanya Alasa"
 "Nias Barat": "Ibu kotanya Mandrehe"
 "Nias Selatan": "Ibu kotanya Telukdalam"
 "Gunungsitoli": "Ibu kota sama"
} 

Daftar berupa daftar di dalam kamus:
daftar_kecamatan = {
 "Nias": ["Gidö", "Idanögawo", "Bawölato"],
 "Nias Utara": ["Alasa", "Lahewa", "Awa'ai"],
 "Nias Barat": ["Mandrehe", "Sirombu", "Lahömi"]
 "Nias Selatan": ["Telukdalam", "Lölömatua", "Gomo"]
 "Gunungsitoli": ["Hilihati", "Pelabuhan Angin", "Afilaza"]
} 

Daftar berupa kamus di dalam kamus:
kabupaten_kota = {
 "Nias": {"data_ada": ["Gidö", "Bawölato"], "belum_ada": ["Hiliserangkai", "Lalai"]},
 "Nias Utara": {"data_ada": ["Alasa", "Lahewa"], "belum_ada": ["Afia", "Olora"]},
 "Nias Barat": {"data_ada": ["Lahömi", "Sirombu"], "belum_ada": ["Mandrehe", "Söu"]},
 "Nias Selatan": {"data_ada": ["Gomo", "Lahusa"], "belum_ada": ["Ambukha", "Holi"]},
 "Gunungsitoli": {"data_ada": ["Afilaza", "Mudik"], "belum_ada": ["Umbu", "Pasar"]},
} 
```
Dari data API yang kita gunakan dalam aplikasi [Gogowaya](https://github.com/sslaia/gogowaya/blob/main/lib/main.dart):
```
[
  {
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
  },
]
```

## Demo mengakses item dari internet dan menampilkannya

Ciptakanlah berkas bernama amaedola.py dalam editor favorit Anda. Dan tulis kode berikut di dalamnya:
```
import requests

data_dari_internet = requests.get("https://my-json-server.typicode.com/sslaia/katawaena/posts").json()

i = 0

while i < len(data_dari_internet):
  for amaedola in data_dari_internet:

    print("| " + str(i + 1) + ": " + amaedola['title'])

    i += 1

```

Silakan menikmati hasilnya. Bak magic, bukan? Kalau melihat kode yang telah saya persiapkan, silakan klik di [Amaedola dari Internet](./latihan/amaedola.py). Nampaknya sbb.:

![Amaedola](./latihan/amaedola.png?raw=true)


### Refleksi

Bagaimana seandainya komponen-komponen di atas (nama, umur, pendidikan) Anda ganti dengan berbagai data Facebook pengguna, menganalisa segala pos, bacaan, like, teman-teman dlsb.? Apakah Anda merasa hal ini fiksi atau nyata?




