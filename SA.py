lokspbu = [20, 35, 55, 60, 75, 90, 120, 125, 135]

loksekarang = 0
totaljarak = 150
kapasitasbk = 35
i = 0

while loksekarang < totaljarak:
    found_spbu = 0
    while i < len(lokspbu) and lokspbu[i] - loksekarang <= kapasitasbk:
        found_spbu = 1
        i += 1
    if found_spbu != 0:
        if lokspbu[i - 1] < totaljarak:  # Cek apakah SPBU di bawah total jarak
            print("Kendaraan mengisi bahan bakar di SPBU:", lokspbu[i - 1])
            loksekarang = lokspbu[i - 1]
        else:
            break  # Keluar dari loop jika SPBU sudah melebihi total jarak
    else:
        break

if loksekarang >= totaljarak:
    print("Berhasil menyelesaikan perjalanan")
