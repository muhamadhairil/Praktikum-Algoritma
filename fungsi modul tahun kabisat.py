def cek_kabisat(tahun):
    """Mengembalikan True jika tahun adalah tahun kabisat."""
    if tahun % 400 == 0:
        return True
    if tahun % 100 == 0:
        return False
    return tahun % 4 == 0


def hari_dalam_bulan(bulan, tahun=None):
    """Mengembalikan jumlah hari dalam sebuah bulan.
    Parameter tahun hanya diperlukan untuk bulan Februari."""
    if bulan == 2:
        return 29 if cek_kabisat(tahun) else 28
    elif bulan in (4, 6, 9, 11):
        return 30
    else:
        return 31


def main():
    print("Program ini akan menentukan jumlah hari dalam bulan tertentu")

    while True:
        print("Masukkan 0 untuk menghentikan program")
        bulan = int(input("masukkan bulan (1-12): "))

        if bulan == 0:
            print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
            break

        if bulan < 1 or bulan > 12:
            print("Bulan tidak valid, masukkan angka 1-12")
            continue

        if bulan == 2:
            tahun = int(input("masukkan tahun (e.g., 2021): "))
            jumlah = hari_dalam_bulan(bulan, tahun)
        else:
            jumlah = hari_dalam_bulan(bulan)

        print(jumlah, "hari dalam sebulan")


main()
    
