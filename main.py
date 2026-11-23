daftar_laporan = []

def tambah_laporan(lokasi, keterangan):
    if not lokasi.strip() or not keterangan.strip():
        print("\n Gagal: Lokasi dan keterangan tidak boleh kosong!")
        return  

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

def ubah_status_laporan(nomor_laporan, status_baru):
    indeks = nomor_laporan - 1
    if 0 <= indeks < len(daftar_laporan):
        daftar_laporan[indeks]["status"] = status_baru
        print(f"\n Sukses: Status laporan nomor {nomor_laporan} berhasil diubah menjadi '{status_baru}'!")
    else:
        print("\n Gagal: Nomor laporan tidak ditemukan.")

while True:
    print("\n=== APLIKASI PELAPORAN KERUSAKAN SEKOLAH ===")
    print("1. Buat laporan baru")
    print("2. Lihat semua laporan") 
    print("3. Ubah status laporan (Pihak Sekolah)")
    print("4. Keluar aplikasi")
    
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == "1":
        input_lokasi = input("\nHarap masukkan lokasi kerusakan: ")
        input_keterangan = input("Harap masukkan keterangan kerusakan: ")
        tambah_laporan(input_lokasi, input_keterangan)
        
    elif pilihan == "2":
        lihat_semua_laporan()
        
    elif pilihan == "3":
        lihat_semua_laporan()
        if len(daftar_laporan) > 0:
            try:
                no_target = int(input("\nMasukkan nomor laporan yang ingin diubah: "))
                print("\nPilih Status Baru:")
                print("1. Dalam Proses Perbaikan")
                print("2. Selesai Diperbaiki")
                pilihan_status = input("Pilih (1/2): ")
                
                if pilihan_status == "1":
                    ubah_status_laporan(no_target, "Dalam Proses Perbaikan")
                elif pilihan_status == "2":
                    ubah_status_laporan(no_target, "Selesai Diperbaiki")
                else:
                    print("\nPilihan status tidak valid.")
            except ValueError:
                print("\n Gagal: Harap masukkan angka yang valid!")
                
    elif pilihan == "4":
        print("\nTerima kasih telah peduli dengan fasilitas sekolah!")
        break
        
    else:
        print("\nPilihan tidak valid, silakan ketik 1, 2, 3, atau 4.")
