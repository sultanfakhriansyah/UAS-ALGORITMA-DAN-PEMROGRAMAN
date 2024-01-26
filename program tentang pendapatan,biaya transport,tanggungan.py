# Program Pendapatan, Tanggungan, dan Biaya Transport

# Input pendapatan
pendapatan = float(input("Masukkan pendapatan bulanan Anda: "))

# Input jumlah tanggungan
tanggungan = int(input("Masukkan jumlah tanggungan: "))

# Input biaya transport
biaya_transport = float(input("Masukkan biaya transport bulanan: "))

# Hitung pendapatan bersih
pendapatan_bersih = pendapatan - biaya_transport

# Hitung rata-rata pendapatan per tanggungan
rata_pendapatan_per_tanggungan = pendapatan / tanggungan if tanggungan != 0 else 0

# Tampilkan hasil
print("\n===== Hasil Perhitungan =====")
print(f"Pendapatan Bulanan: Rp {pendapatan:,.2f}")
print(f"Biaya Transport Bulanan: Rp {biaya_transport:,.2f}")
print(f"Pendapatan Bersih: Rp {pendapatan_bersih:,.2f}")
print(f"Jumlah Tanggungan: {tanggungan}")
print(f"Rata-rata Pendapatan per Tanggungan: Rp {rata_pendapatan_per_tanggungan:,.2f}")

# Evaluasi kondisi keuangan
if rata_pendapatan_per_tanggungan < 1000000:
    print("\nKondisi keuangan Anda perlu diperhatikan, rata-rata pendapatan per tanggungan kurang dari Rp 1.000.000.")
else:
    print("\nKondisi keuangan Anda stabil, rata-rata pendapatan per tanggungan mencukupi.")
