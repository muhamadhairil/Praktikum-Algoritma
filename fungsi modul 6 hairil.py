def konversi_nilai(huruf="E"):
    """Mengubah huruf nilai menjadi angka.
    Default argument: jika huruf tidak diberikan, dianggap 'E' (0)."""
    skala = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}
    return skala.get(huruf.upper(), 0)


def hitung_rata_rata(daftar_nilai, pembulatan=1):
    """Menghitung rata-rata. Default argument: pembulatan = 1 angka desimal."""
    if len(daftar_nilai) == 0:
        return 0.0
    return round(sum(daftar_nilai) / len(daftar_nilai), pembulatan)


def main():
    daftar_nilai = []

    while True:
        huruf = input("masukkan nilai: ").strip()
        if huruf == "":
            break

        angka = konversi_nilai(huruf)
        print("nilai =", angka)
        daftar_nilai.append(angka)

    rata_rata = hitung_rata_rata(daftar_nilai)
    print("Rata-ratanya adalah: ", rata_rata)


main()
