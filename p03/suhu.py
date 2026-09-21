data_suhu = [28.5, 30.2, 29.8, 31.0, 27.9]

def hitung_rata_rata(data):
    """Menghitung rata-rata dari sebuah list angka.
    Input: data (list angka)
    Output: rata-rata (float)
    """
    total = 0
    for i in range(len(data)):
        total = total + data[i]
    return total / len(data)

def cari_tertinggi(data):
    """Mencari nilai tertinggi dari sebuah kumpulan angka.
    Input: data (list angka)
    Output: nilai tertinggi (float/int)
    """
    tertinggi = data[0]
    for nilai in data:
        if nilai > tertinggi:
            tertinggi = nilai
    return tertinggi

def cek_status(suhu):
    """Menentukan status suhu berdasarkan ambang batas:
    - PANAS  : suhu > 30
    - NORMAL : 25 <= suhu <= 30
    - DINGIN : suhu < 25
    Input: suhu (float/int)
    Output: kategori status (string)
    """
    if suhu > 30:
        return "PANAS"
    elif suhu >= 25:
        return "NORMAL"
    else:
        return "DINGIN"

if __name__ == "__main__":
    rata = hitung_rata_rata(data_suhu)
    print("Rata-rata:", rata)
    print("Tertinggi :", cari_tertinggi(data_suhu))
    print("Status   :", cek_status(rata))