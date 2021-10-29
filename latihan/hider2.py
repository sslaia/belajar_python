import json


def menginput_menu():
    data_makanan = []
    
    selesai = False
    
    while selesai == False:
        nama_makanan = input("Masukkan nama makanan : ") 
        harga_makanan = int(input("Masukkan harga        : "))

        data_makanan.append({"nama": nama_makanan, "harga": harga_makanan})

        pertanyaan = input("Masih ada lagi? y/t : ")

        if pertanyaan == "y":
            selesai = False
        else:
            selesai = True
            with open('hider_menu.json', 'w') as json_file:
            json.dump(data_makanan, json_file)

def menginput_transaksi():
    data_transaksi = []
    
    selesai = False
    
    while selesai == False:
        tanggal =  input("Masukkan tanggal      : ")
        item_makanan = input("Masukkan nama makanan : ") 
        jumlah =  input("Masukkan jumlah       : ")
        total_harga = int(input("Masukkan harga        : "))
        
        data_transaksi.append({tanggal: "", item_makanan: "", jumlah: "", total_harga: ""})
        
        pertanyaan = input("Masih ada lagi? y/t : ")

        if pertanyaan == "y":
            selesai = False
        else:
            selesai = True
            # simpan data yang telah ada ke dalam database        
    	    with open('hider_transaksi.json', 'w') as json_file:
            json.dump(data_transaksi, json_file)

def menginput_anggota():
    data_anggota = []
    
    selesai = False
    
    while selesai == False:
        nama = input("Masukkan nama makanan : ") 
        nomor = input("Masukkan harga        : ")
        
        data_anggota.append({nama: "", nomor: ""})
        
        pertanyaan = input("Masih ada lagi? y/t : ")

        if pertanyaan == "y":
            selesai = False
        else:
            selesai = True
            # simpan data yang telah ada ke dalam database
            with open('hider_anggota.json', 'w') as json_file:
            json.dump(data_anggota, json_file)
        
# Mulai dari sini program

print("Pilihan aksi")
print()
print("1. Menginput transaksi")
print("2. Menginput anggota")
print("3. Menginput menu")
print()
pilihan = input("Silakan memilih: (1/2/3) ")

if pilihan == "3":
    menginput_menu()
elif pilihan == "2":
    menginput_anggota()
else:
    menginput_transaksi()





# with open('toko_hider.json') as json_file:
#     data = json.load(json_file)


# {
#     "daftar_menu": [],
#     "daftar_transaksi": []
#     "daftar_anggota": []
# }

# 1. Daftar transaksi

# tanggal, item_makanan, jumlah, total


# {
# [{tanggal: "", item: "", jumlah: "", total: ""}]
# }



# 2. Daftar menu



# {
#     [{nama: "Gore gae", harga: 1000}, {nama: "Gado-gado", harga: 1500}, {nama: "Kopi susu", harga: 2000}, {nama: "Teh manis", harga: 2500}]
# }







# [Gore gae, Gado-gado, Kopi susu, Teh manis]

#    data_makanan.append({nama: "Gore gae", harga: 1000}, {nama: "Gado-gado", harga: 1500}, {nama: "Kopi susu", harga: 2000}, {nama: "Teh manis", harga: 2500})

