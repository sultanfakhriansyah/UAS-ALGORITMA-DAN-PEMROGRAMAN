# Inisialisasi list untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menghitung nilai rata-rata
def hitung_rata_rata(nilai):
    total_nilai = sum(nilai)
    rata_rata = total_nilai / len(nilai)
    return rata_rata

# Input jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Input data nilai untuk setiap mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nMasukkan data untuk mahasiswa ke-{i+1}:")
    nama_mahasiswa = input("Nama: ")
    nilai_mahasiswa = []

    # Input nilai mata kuliah
    for j in range(3):  # Anggap saja ada 3 mata kuliah
        nilai = float(input(f"Masukkan nilai mata kuliah ke-{j+1}: "))
        nilai_mahasiswa.append(nilai)

    # Hitung rata-rata nilai
    rata_rata_nilai = hitung_rata_rata(nilai_mahasiswa)

    # Simpan data mahasiswa ke dalam list
    data_mahasiswa.append({
        'Nama': nama_mahasiswa,
        'Nilai': nilai_mahasiswa,
        'Rata-rata Nilai': rata_rata_nilai
    })

# Tampilkan data mahasiswa
print("\nData Mahasiswa:")
for mahasiswa in data_mahasiswa:
    print(f"\nNama: {mahasiswa['Nama']}")
    print(f"Nilai: {mahasiswa['Nilai']}")
    print(f"Rata-rata Nilai: {mahasiswa['Rata-rata Nilai']}")

# Tambahan: Tampilkan rata-rata nilai seluruh mahasiswa
rata_rata_seluruh_mahasiswa = hitung_rata_rata([mahasiswa['Rata-rata Nilai'] for mahasiswa in data_mahasiswa])
print(f"\nRata-rata Nilai Seluruh Mahasiswa: {rata_rata_seluruh_mahasiswa}")
