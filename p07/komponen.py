from gpiozero import AngularServo
from perangkat import Aktuator, Sensor
from statistik import rata_rata, tertinggi
from validasi import BATAS_ATAS, BATAS_BAWAH, dalam_rentang


class Servo(Aktuator):

    def __init__(self, nama, nilai_awal=0, pin=None):
        super().__init__(nama, nilai_awal)
        self.perangkat = None
        if pin is not None:
            self.perangkat = AngularServo(
                pin, initial_angle=nilai_awal, min_angle=0, max_angle=180
            )

    def gerak_ke(self, sudut):
        if not dalam_rentang(sudut, 0, 180):
            raise ValueError("sudut harus 0 sampai 180")
        self.nilai = sudut
        if self.perangkat is not None:
            self.perangkat.angle = sudut

    def lebar_pulsa(self):
        if self.perangkat is None:
            return None
        return round(self.perangkat.pulse_width * 1000, 3)

    def proses(self):
        return self.nilai


class SensorSuhu(Sensor):

    def __init__(self, nama, satuan="C"):
        super().__init__(nama, satuan)

    def proses(self):
        return tertinggi(self.data)


class Mikrofon(Sensor):

    def __init__(self, nama, satuan="dB"):
        super().__init__(nama, satuan)

    def baca(self, nilai):
        if not dalam_rentang(nilai, BATAS_BAWAH, BATAS_ATAS):
            raise ValueError("level di luar rentang")
        super().baca(nilai)

    def proses(self):
        return rata_rata(self.data)


class LampuIndikator(Aktuator):

    def __init__(self, nama, nilai_awal=0):
        super().__init__(nama, nilai_awal)

    def atur(self, nilai):
        self.nilai = nilai

    def proses(self):
        return self.nilai