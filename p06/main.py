from komponen import Mikrofon, SensorSuhu, Servo

mik = Mikrofon("mik-1")
suhu = SensorSuhu("suhu-servo")
alis = Servo("alis", 90)

mik.baca(40.0)
mik.baca(55.0)
mik.baca(70.0)

suhu.baca(31.5)
suhu.baca(36.0)
suhu.baca(33.2)

alis.gerak_ke(120)

daftar = [mik, suhu, alis]
for p in daftar:
  p.nyalakan()
  hasil = p.proses()    
  print(p, "->", hasil)

from komponen import LampuIndikator

# Membuat objek LampuIndikator dengan nama "led-uji"
lampu = LampuIndikator("led-uji")

# Skenario 1: Input normal di dalam rentang (80)
lampu.atur(80)
print("Hasil atur(80) :", lampu.proses  ())

# Skenario 2: Input melebihi batas maksimum (150)
lampu.atur(150)
print("Hasil atur(150):", lampu.proses())

# Skenario 3: Input di bawah batas minimum (-5)
lampu.atur(-5)
print("Hasil atur(-5) :", lampu.proses())