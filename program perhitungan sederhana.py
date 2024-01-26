# Program perhitungan sederhana dalam Python

# Fungsi untuk penjumlahan
def tambah(a, b):
    return a + b

# Fungsi untuk pengurangan
def kurang(a, b):
    return a - b

# Fungsi untuk perkalian
def kali(a, b):
    return a * b

# Fungsi untuk pembagian
def bagi(a, b):
    # Menghindari pembagian oleh nol
    if b != 0:
        return a / b
    else:
        return "Tidak dapat melakukan pembagian oleh nol"

# Meminta pengguna memasukkan dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Menampilkan hasil perhitungan
print("Hasil penjumlahan:", tambah(angka1, angka2))
print("Hasil pengurangan:", kurang(angka1, angka2))
print("Hasil perkalian:", kali(angka1, angka2))
print("Hasil pembagian:", bagi(angka1, angka2))