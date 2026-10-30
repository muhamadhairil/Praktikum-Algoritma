def nilai_huruf(huruf):
    tabel = {
        "A": 4,
        "A-": 3.75,
        "B+": 3.5,
        "B": 3,
        "B-": 2.75,
        "C+": 2.5,
        "C": 2,
        "C-": 1.75,
        "D": 1.5,
        "E": 1.25,
    }
    return tabel.get(huruf.upper())


def rata_rata(daftar):
    return sum(daftar) / len(daftar)


daftar_nilai = []

while True:
    huruf = input("masukkan nilai: ").strip()

    
    if huruf == "":
        break

    angka = nilai_huruf(huruf)
    print("nilai =", angka)

    if angka is not None:
        daftar_nilai.append(angka)

if len(daftar_nilai) > 0:
    print("rata - rata nya adalah: ", rata_rata(daftar_nilai))
else:
    print("tidak ada nilai yang valid")
