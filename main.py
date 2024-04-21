from services.pemesanan import pesan_tiket

def main():
    print("Selamat datang di Aplikasi Pemesanan Tiket Bis Online")
    print("=====================================================")

    # Meminta input dari pengguna
    kelas = input("Pilih kelas (Ekonomi/Bisnis/Eksekutif): ")
    jenis = input("Pilih jenis (Antar Kota/Antar Provinsi): ")
    rute = input("Pilih rute (contoh: Jakarta - Surabaya): ")

    # Melakukan pemesanan tiket
    ringkasan_pemesanan = pesan_tiket(kelas, jenis, rute)

    # Menampilkan ringkasan pemesanan
    print("\nRingkasan Pemesanan:")
    print("====================")
    print("Kelas: ", ringkasan_pemesanan["kelas"])
    print("Jenis: ", ringkasan_pemesanan["jenis"])
    print("Rute: ", ringkasan_pemesanan["rute"])
    print("Total Biaya: Rp", ringkasan_pemesanan["total_biaya"])

if __name__ == "__main__":
    main()
