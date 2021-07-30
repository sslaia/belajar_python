# Aplikasi untuk menghitung indeks berat badan

print("\n\nYa'ahowu, kawa.\n")
print("Dengan aplikasi sederhana ini Anda bisa memeriksa.")
print("entah Anda memiliki berat badan ideal")
print("atau Anda agak kekurusan/kegemukan.\n")

berat = float(input("Berat badan Anda dalam kg: "))
tinggi = float(input("Tinggi Anda dalam cm:      "))

bmi = berat / (tinggi/100) ** 2
nilai = round(bmi, 2)

print("\n\nTerima kasih.\n")
print("Berikut hasil evaluasi indeks berat badan Anda:\n\n")
print("Nilai indeks Anda: " + str(nilai))

if bmi < 18.50:
    print("Nampaknya Anda agak kekurusan")

if bmi > 25:
    print("Nampaknya Anda agak kegemukan")

if bmi > 18.50 and bmi < 25:
    print("Selamat. Anda memiliki berat badan ideal!")






# BMI = mass(kg) / height(m2)
# underweight < 18.5
# overweight > 25
