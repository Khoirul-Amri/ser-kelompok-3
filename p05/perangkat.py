class perangkat:

    def __init__(self, nama):
        self.nama = nama
        self.aktif = False

    def nyalakan(self):
        self.aktif = True

    def matikan(self):
        self.aktif = False

    def proses(self):
        raise NotImplementedError("class turunan harus menulis proses()")

    def __str__(self):
        if self.aktif:
            status = "ON"
        else:
            status = "OFF"
        return f"{self.nama} [{status}]"

class sensor(perangkat):
    def __init__(self, nama,satuan):
        super().__init__(nama)
        self.satuan = satuan
        self.data = []

    def baca(self, nilai):
        self.data.append(nilai)

class aktuator(perangkat):
    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan
        self.data = []

    def baca(self,nilai):
        self.data.append(nilai)

class aktuator(perangkat):
    def __init__(self, nama, nilai_awal=0):
        super().__init__(nama)
        self.nilai = nilai_awal            


if __name__=="__main__":
    s = sensor("sensor-uji", "dB")
    a = aktuator("aktuator-uji", 10)
    s.nyalakan()
    print(s)
    print(a)
    print(isinstance(s, sensor))
    print(isinstance(s, perangkat))  
    print(isinstance(s, aktuator))
    s.baca(40.0)
    s.baca(50.0)
    print(s.data) 
    a.nyalakan()
    print(a)