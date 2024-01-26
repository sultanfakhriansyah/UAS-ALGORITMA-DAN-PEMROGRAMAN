# Program Daftar Pembelian Tiket Kereta Api

class TiketKereta:
    def __init__(self, nama, tujuan, jadwal, jumlah_tiket):
        self.nama = nama
        self.tujuan = tujuan
        self.jadwal = jadwal
        self.jumlah_tiket = jumlah_tiket

    def hitung_biaya(self):
        # Harga tiket per orang
        harga_per_tiket = 150000

        # Hitung total biaya
        total_biaya = harga_per_tiket * self.jumlah_tiket
        return total_biaya

def main():
    print("Selamat datang di Layanan Pemesanan Tiket Kereta Api")
    print("Silakan masukkan informasi pemesanan:")
    
    # Input data pelanggan
    nama_pelanggan = input("Nama Pelanggan: ")
    tujuan_perjalanan = input("Tujuan Perjalanan: ")
    jadwal_perjalanan = input("Jadwal Perjalanan: ")
    jumlah_tiket = int(input("Jumlah Tiket: "))

    # Membuat objek TiketKereta
    tiket = TiketKereta(nama_pelanggan, tujuan_perjalanan, jadwal_perjalanan, jumlah_tiket)

    # Menampilkan ringkasan pemesanan
    print("\nRingkasan Pemesanan:")
    print(f"Nama Pelanggan: {tiket.nama}")
    print(f"Tujuan Perjalanan: {tiket.tujuan}")
    print(f"Jadwal Perjalanan: {tiket.jadwal}")
    print(f"Jumlah Tiket: {tiket.jumlah_tiket}")
    print(f"Total Biaya: Rp {tiket.hitung_biaya()}")

if __name__ == "__main__":
    main()
