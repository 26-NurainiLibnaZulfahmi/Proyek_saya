daftar_laporan = []

def tambah_laporan(lokasi, keterangan):
    laporan_baru = {
        "lokasi": lokasi,
        "keterangan": keterangan,
        "status": "Sedang menunggu perbaikan"
    }
    daftar_laporan.append(laporan_baru)
    print(f"\n Sukses: Laporan anda di '{lokasi}' telah terkirim pada pihak sekolah!")

def lihat_semua_laporan():
    print("\n=== DAFTAR LAPORAN KERUSAKAN SEKOLAH ===")
    if len(daftar_laporan) == 0:
        print("Belum ada laporan kerusakan yang masuk.")
    else:
        for nomor, laporan in enumerate(daftar_laporan, start=1):
            print(f"\n[Laporan #{nomor}]")
            print(f" Lokasi     : {laporan['lokasi']}")
            print(f" Keterangan : {laporan['keterangan']}")
            print(f" Status     : {laporan['status']}")
            print("-" * 30)

while True:
    print("\n=== APLIKASI PELAPORAN KERUSAKAN SEKOLAH ===")
    print("1. Buat laporan kembali")
    print("2. Lihat semua laporan") 
    print("3. Keluar aplikasi")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        input_lokasi = input("\nHarap masukkan lokasi kerusakan: ")
        input_keterangan = input("Harap masukkan keterangan kerusakan: ")
        tambah_laporan(input_lokasi, input_keterangan)
        
    elif pilihan == "2":
        lihat_semua_laporan()
        
    elif pilihan == "3":
        print("\nTerima kasih telah peduli dengan fasilitas sekolah!")
        break
        
    else:
        print("\nPilihan tidak valid, silakan ketik 1, 2, atau 3.")
