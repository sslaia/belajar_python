import json


def menginput_menu():
    data_makanan = []
    
    nama_makanan = input("Masukkan nama makanan : ") 
    harga_makanan = int(input("Masukkan harga        : "))

    data_makanan.append({"nama": nama_makanan, "harga": harga_makanan})

    with open('toko_hider.json', 'w') as json_file:
        json.dump(data_makanan, json_file)
        json_file.close()

def menginput_transaksi():
    data_transaksi = []
    
    tanggal =  input("Masukkan tanggal      : ")
    item_makanan = input("Masukkan nama makanan : ") 
    jumlah =  input("Masukkan jumlah       : ")
    total_harga = int(input("Masukkan harga        : "))

    data_transaksi.append({tanggal: "", item_makanan: "", jumlah: "", total_harga: ""})

    with open('toko_hider.json', 'w') as json_file:
        data_transaksi = json.dump(json_file)

def menginput_anggota():
    data_anggota = []
    
    nama = input("Masukkan nama makanan : ") 
    nomor = input("Masukkan harga        : ")

    data_anggota.append({nama: "", nomor: ""})

    with open('toko_hider.json', 'w') as json_file:
        data_anggota = json.dump(json_file)


menginput_menu()





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

