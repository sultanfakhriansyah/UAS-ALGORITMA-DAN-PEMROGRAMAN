class PenjualanMotor:
    def __init__(self, merk, jumlah_terjual, harga_satuan):
        self.merk = merk
        self.jumlah_terjual = jumlah_terjual
        self.harga_satuan = harga_satuan

    def hitung_total_penjualan(self):
        return self.jumlah_terjual * self.harga_satuan

def main():
    print("Program Catatan Penjualan Motor Yamaha")
    print("-------------------------------------")

    # Membuat objek penjualan untuk setiap model motor
    xmax = PenjualanMotor("XMax", 10, 30000000)
    mio = PenjualanMotor("Mio", 15, 15000000)
    aerox = PenjualanMotor("Aerox", 8, 25000000)

    # Menyimpan objek dalam list
    penjualan_motor = [xmax, mio, aerox]

    # Menampilkan model motor yang tersedia
    print("\nModel Motor yang Tersedia:")
    for i, motor in enumerate(penjualan_motor, 1):
        print(f"{i}. {motor.merk}")

    # Meminta input pengguna untuk memilih model motor
    pilihan_motor = int(input("\nPilih nomor model motor untuk diketahui penjualannya: "))
    motor_terpilih = penjualan_motor[pilihan_motor - 1]

    # Menampilkan hasil penjualan untuk model motor yang dipilih
    print(f"\nModel: {motor_terpilih.merk}")
    print(f"Jumlah Terjual: {motor_terpilih.jumlah_terjual}")
    print(f"Harga Satuan: ${motor_terpilih.harga_satuan}")
    print(f"Total Penjualan: ${motor_terpilih.hitung_total_penjualan()}")

    # Menghitung total penjualan keseluruhan
    total_semua_penjualan = sum(motor.hitung_total_penjualan() for motor in penjualan_motor)
    print("\nTotal Penjualan Keseluruhan:", total_semua_penjualan)

if __name__ == "__main__":
    main()
