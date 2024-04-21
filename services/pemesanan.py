from models.tiket_bis import TiketBis
import json

def pesan_tiket(kelas, jenis, rute):
    # Membuat objek TiketBis
    tiket = TiketBis(kelas, jenis, rute)

    # Memuat data rute dari file JSON
    with open("data/rute.json", "r") as file:
        rute_data = json.load(file)

    # Menghitung biaya
    total_biaya = tiket.hitung_biaya(rute_data)

    # Mengembalikan ringkasan pemesanan
    return {
        "kelas": tiket.kelas,
        "jenis": tiket.jenis,
        "rute": tiket.rute,
        "total_biaya": total_biaya
    }
