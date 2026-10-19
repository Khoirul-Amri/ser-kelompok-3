def rata_rata(data):
    return sum(data) / len(data)

def tertinggi(data):
    return max(data)

def terendah(data):
    return min(data)

def rentang(data):
    return (min(data), max(data))

def ringkasan(data):
    return {
        "jumlah": len(data),
        "rata": round(rata_rata(data), 2),
        "min": min(data),
        "maks": max(data),
        "median": median(data),
    }

def median(data):
    data_urut = sorted(data)
    n = len(data_urut)
    mid = n // 2
    if n % 2 == 1:
        return data_urut[mid]
    else:
        return (data_urut[mid - 1] + data_urut[mid]) / 2