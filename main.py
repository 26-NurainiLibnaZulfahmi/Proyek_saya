daftar_laporan = []

def tambah_laporan(lokasi, keterangan):
    laporan_baru = {
        "lokasi": lokasi,
        "keterangan": keterangan,
        "status": "Sedang menunggu perbaikan"
    }
    daftar_laporan.append(laporan_baru)
    print(f"\n Sukses: Laporan anda di '{lokasi}' telah terkirim pada pihak sekolah!")

while True:
    print("\n=== APLIKASI PELAPORAN KERUSAKAN SEKOLAH ===")
    print("1. Buat laporan kembali")
    print("2. Keluar aplikasi")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        input_lokasi = input("\nHarap masukkan lokasi kerusakan: ")
        input_keterangan = input("Harap masukkan keterangan kerusakan: ")
        tambah_laporan(input_lokasi, input_keterangan)
        
    elif pilihan == "2":
        print("\nTerima kasih telah peduli dengan fasilitas sekolah!")
        break
        
    else:
        print("\nPilihan tidak valid, silakan ketik 1 atau 2.")
