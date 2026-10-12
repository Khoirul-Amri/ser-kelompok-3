from perangkat import sensor, aktuator
from statistik import rata_rata, tertinggi
class mikrofon(sensor):
    def __init__(self, nama):
        super().__init__(nama, "dB")

    def proses(self):
        return rata_rata(self.data)

class sensorsuhu(sensor):
    def __init__(self, nama):
        super().__init__(nama, "c")

    def proses(self):
        return tertinggi(self.data)

class servo(aktuator):
    def gerak_ke(self, sudut):
        if sudut < 0:
            sudut = 0
        if sudut > 180:
            sudut =180
        self.nilai = sudut

    def proses(self):
        return self.nilai

class LampuIndikator(servo):
    def atur(self, nilai):
        if nilai < 0:
            nilai = 0
        if nilai > 100:
            nilai = 100
        self.nilai = nilai

    def proses(self):
        return self.nilai


from komponen import mikrofon,sensorsuhu, servo, LampuIndikator

mik = mikrofon("mik-1")
suhu = sensorsuhu("suhu-servo")
alis = servo("alis",90)
lampu = LampuIndikator("lampu-1")

mik.baca(40.0)
mik.baca(55.0)
mik.baca(70.0)
suhu.baca(31.5)
suhu.baca(36.0)
suhu.baca(36.2)
alis.gerak_ke(120)
lampu.atur(80)

daftar = [mik, suhu, alis, lampu]

for p in daftar:
    p.nyalakan()
    hasil = p.proses()
    print(p, "->", hasil)
    
print("--- Uji LampuIndikator ---")

lampu.atur(80)
print("Hasil atur(80):", lampu.proses())

lampu.atur(150)
print("Hasil atur(150):", lampu.proses())

lampu.atur(-5)
print("Hasil atur(-5):", lampu.proses())    