class TiketBis:
    def __init__(self, kelas, jenis, rute):
        self.kelas = kelas
        self.jenis = jenis
        self.rute = rute

    def hitung_biaya(self, rute_data):
        biaya = 0
        # Hitung biaya berdasarkan rute dari data JSON
        biaya += rute_data.get(self.rute, 0)

        # Biaya berdasarkan kelas
        if self.kelas == "Ekonomi":
            biaya += 100000
        elif self.kelas == "Bisnis":
            biaya += 150000
        elif self.kelas == "Eksekutif":
            biaya += 200000

        # Biaya tambahan untuk jenis bis antar provinsi
        if self.jenis == "Antar Provinsi":
            biaya += 50000

        return biaya
