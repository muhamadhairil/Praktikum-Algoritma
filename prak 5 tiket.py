def harga_tiket(umur):
    if umur <= 2:
        return 0
    elif umur <= 12:        
        return 14
    elif umur >= 65:
        return 18
    else:                   
        return 23


total = 0


while True:
    teks = input("masukkan umur: ").strip()

    if teks == "":          
        break

    if not teks.isdigit():  
        print("Umur tidak valid, coba lagi")
        continue

    umur = int(teks)
    harga = harga_tiket(umur)

    if harga == 0:
        print("Gratis")
    else:
        print(f"Harga ${harga:.2f}")

    total += harga
    print(f"Running total: {total:.2f}")


while True:
    uang = float(input("masukkan jumlah uang: "))

    if uang >= total:
        break
    print(f"Uang kurang ${total - uang:.2f}, coba lagi")

print(f"Running kembalian: {uang - total:.2f}")
