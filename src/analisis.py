def hitung_rata_rata(daftar_nilai):
    if not daftar_nilai:
        return 0.0
    return sum(daftar_nilai) / len(daftar_nilai)

def tentukan_predikat(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"
