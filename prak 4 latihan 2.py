def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)


def jumlah_hari(bulan, tahun):
    if bulan == 2:
        return 29 if tahun_kabisat(tahun) else 28
    elif bulan in (4, 6, 9, 11):
        return 30
    else:
        return 31


nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

lagi = "y"

while lagi.lower() == "y":
   
    bulan = 0
    while bulan < 1 or bulan > 12:
        bulan = int(input("Masukkan bulan (1-12): "))
        if bulan < 1 or bulan > 12:
            print("Bulan tidak valid! Masukkan angka 1 sampai 12.")
    
    tahun = 0
    while tahun <= 0:
        tahun = int(input("Masukkan tahun: "))
        if tahun <= 0:
            print("Tahun tidak valid! Masukkan angka positif.")

    hari = jumlah_hari(bulan, tahun)
    print(f"\nBulan {nama_bulan[bulan - 1]} {tahun} memiliki {hari} hari.\n")

    lagi = input("Hitung lagi? (y/t): ")

print("Terima kasih!")
