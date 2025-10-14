pelanggan_db = []
sukucadang_db = []
workorder_db = []
id_pelanggan_selanjutnya = 1
id_wo_selanjutnya = 1
program_jalan = True
print('==============================================')
print('         PROGRAM SERVIS KENDARAAN         ')
print('==============================================')

while program_jalan:
    print('\n========= MENU UTAMA =========')
    print('--- INPUT DATA ---')
    print('1. Tambah Pelanggan Baru')
    print('2. Buat Work Order (WO) Baru')
    print('3. Tambah Suku Cadang ke Stok')

    print('\n--- LIHAT DATA ---')
    print('4. Lihat Riwayat Servis Kendaraan')
    print('5. Lihat Stok Suku Cadang')
    print('6. Lihat Kendaraan yang Sedang Dikerjakan')

    print('\n--- UBAH DATA ---')
    print('7. Ubah Status Work Order')
    print('8. Tambah Catatan untuk Work Order')
    print('9. Ubah Data Pelanggan')

    print('\n--- HAPUS DATA ---')
    print('10. Hapus Suku Cadang dari Stok')
    print('11. Hapus (Batalkan) Work Order')

    print('\n0. KELUAR APLIKASI')
    pilihan = input('Masukkan pilihan Anda: ')
    if pilihan == '1':
        print('\n--- [1] Tambah Pelanggan Baru ---')
        nama = input('Masukkan nama pelanggan: ')
        hp = input('Masukkan nomor HP: ')
        
        pelanggan_db.append((id_pelanggan_selanjutnya, nama, hp))
        print(f'\nBerhasil. Pelanggan "{nama}" telah disimpan dengan ID {id_pelanggan_selanjutnya}.')
        id_pelanggan_selanjutnya += 1
    elif pilihan == '2':
        print('\n--- [2] Buat Work Order (WO) Baru ---')
        if len(pelanggan_db) == 0:
            print(' Belum ada data pelanggan. Silakan tambah pelanggan terlebih dahulu.')
        else:
            id_pelanggan_str = input('Masukkan ID pelanggan: ')
            nopol = input('Masukkan nomor polisi kendaraan: ').upper()
            apakah_angka = True
            if len(id_pelanggan_str) > 0:
                for karakter in id_pelanggan_str:
                    if karakter not in '0123456789':
                        apakah_angka = False
                        break
            else:
                apakah_angka = False
            
            if apakah_angka:
                id_pelanggan = int(id_pelanggan_str)

                pelanggan_ada = False
                for p in pelanggan_db:
                    if p[0] == id_pelanggan:
                        pelanggan_ada = True
                        break
                
                if pelanggan_ada:
                    kendaraan_sedang_dikerjakan = False
                    for wo in workorder_db:
                        if wo[2] == nopol and wo[3] == 'Dikerjakan':
                            kendaraan_sedang_dikerjakan = True
                            break
                    
                    if kendaraan_sedang_dikerjakan:
                        print(f'Gagal. Kendaraan {nopol} statusnya sudah "Dikerjakan".')
                    else:
                        workorder_db.append((id_wo_selanjutnya, id_pelanggan, nopol, 'Dikerjakan', ''))
                        print(f'\nBerhasil. Work Order (ID: {id_wo_selanjutnya}) untuk kendaraan {nopol} telah dibuat.')
                        id_wo_selanjutnya += 1
                else:
                    print(f'Gagal. Pelanggan dengan ID {id_pelanggan} tidak ditemukan.')
            else:
                print('Gagal. ID Pelanggan harus berupa angka.')

    elif pilihan == '3':
        print('\n--- [3] Tambah Suku Cadang ke Stok ---')
        id_barang_str = input('Masukkan ID barang (angka): ')
        nama_barang = input('Masukkan nama barang: ')
        stok_str = input('Masukkan jumlah stok: ')

        id_benar = True
        if len(id_barang_str) > 0:
            for karakter in id_barang_str:
                if karakter not in '0123456789':
                    id_benar = False
                    break
        else:
            id_benar = False
            
        stok_benar = True
        if len(stok_str) > 0:
            for karakter in stok_str:
                if karakter not in '0123456789':
                    stok_benar = False
                    break
        else:
            stok_benar = False

        if id_benar and stok_benar:
            id_barang = int(id_barang_str)
            stok = int(stok_str)

            id_sudah_ada = False
            for sc in sukucadang_db:
                if sc[0] == id_barang:
                    id_sudah_ada = True
                    break
            
            if id_sudah_ada:
                print(f'Gagal. ID barang {id_barang} sudah digunakan.')
            else:
                sukucadang_db.append((id_barang, nama_barang, stok))
                print(f'\nBerhasil. Barang "{nama_barang}" (ID: {id_barang}) sudah ditambahkan ke gudang.')
        else:
            print('Gagal. ID barang dan stok harus berupa angka.')

    elif pilihan == '4':
        print('\n--- [4] Lihat Riwayat Servis Kendaraan ---')
        nopol = input('Masukkan nomor polisi: ').upper()
        
        ada_riwayat = False
        print(f'\n--- Hasil Pencarian untuk {nopol} ---')
        for wo in workorder_db:
            if wo[2] == nopol:
                nama_pelanggan = 'Tidak Diketahui'
                for p in pelanggan_db:
                    if p[0] == wo[1]:
                        nama_pelanggan = p[1]
                        break
                print(f"ID WO: {wo[0]}, Pelanggan: {nama_pelanggan}, Status: {wo[3]}, Catatan: {wo[4]}")
                ada_riwayat = True
        
        if ada_riwayat == False:
            print(f'Tidak ada riwayat servis untuk kendaraan {nopol}.')

    elif pilihan == '5':
        print('\n--- [5] Lihat Stok Suku Cadang ---')
        if len(sukucadang_db) == 0:
            print('Stok suku cadang masih kosong.')
        else:
            print('ID | Nama Barang | Stok')
            print('--------------------------')
            for sc in sukucadang_db:
                print(f"{sc[0]} | {sc[1]} | {sc[2]}")

    elif pilihan == '6':
        print('\n--- [6] Lihat Kendaraan yang Sedang Dikerjakan ---')
        ada_yang_dikerjakan = False
        for wo in workorder_db:
            if wo[3] == 'Dikerjakan':
                print(f"ID WO: {wo[0]}, Nopol: {wo[2]}, Status: {wo[3]}")
                ada_yang_dikerjakan = True
        
        if ada_yang_dikerjakan == False:
            print('Saat ini tidak ada kendaraan yang sedang dikerjakan.')

    elif pilihan == '7':
        print('\n--- [7] Ubah Status Work Order ---')
        id_wo_str = input('Masukkan ID Work Order yang akan diubah: ')
        
        apakah_angka = True
        if len(id_wo_str) > 0:
            for karakter in id_wo_str:
                if karakter not in '0123456789':
                    apakah_angka = False
                    break
        else:
            apakah_angka = False
        
        if apakah_angka:
            id_wo = int(id_wo_str)
            index_ketemu = -1
            for i in range(len(workorder_db)):
                if workorder_db[i][0] == id_wo:
                    index_ketemu = i
                    break
            
            if index_ketemu > -1:
                wo_lama = workorder_db[index_ketemu]
                print(f'Status saat ini untuk WO ID {id_wo} adalah "{wo_lama[3]}"')
                status_baru = input('Masukkan status baru (contoh: Selesai, Menunggu Sparepart): ')
                
                wo_update = (wo_lama[0], wo_lama[1], wo_lama[2], status_baru, wo_lama[4])
                workorder_db[index_ketemu] = wo_update
                print(f'\nBerhasil. Status WO ID {id_wo} telah diubah menjadi "{status_baru}".')
            else:
                print(f'Gagal. Work Order dengan ID {id_wo} tidak ditemukan.')
        else:
            print('Gagal. ID Work Order harus berupa angka.')

    elif pilihan == '8':
        print('\n--- [8] Tambah Catatan untuk Work Order ---')
        id_wo_str = input('Masukkan ID Work Order: ')

        apakah_angka = True
        if len(id_wo_str) > 0:
            for karakter in id_wo_str:
                if karakter not in '0123456789':
                    apakah_angka = False
                    break
        else:
            apakah_angka = False
            
        if apakah_angka:
            id_wo = int(id_wo_str)
            index_ketemu = -1
            for i in range(len(workorder_db)):
                if workorder_db[i][0] == id_wo:
                    index_ketemu = i
                    break
            
            if index_ketemu > -1:
                catatan = input('Tulis catatan dari montir: ')
                wo_lama = workorder_db[index_ketemu]
                wo_update = (wo_lama[0], wo_lama[1], wo_lama[2], wo_lama[3], catatan)
                workorder_db[index_ketemu] = wo_update
                print(f'\n Berhasil. Catatan untuk WO ID {id_wo} sudah disimpan.')
            else:
                print(f'Gagal. Work Order dengan ID {id_wo} tidak ditemukan.')
        else:
            print('Gagal. ID Work Order harus berupa angka.')

    elif pilihan == '9':
        print('\n--- [9] Ubah Data Pelanggan ---')
        id_p_str = input('Masukkan ID pelanggan yang akan diubah: ')
        
        apakah_angka = True
        if len(id_p_str) > 0:
            for karakter in id_p_str:
                if karakter not in '0123456789':
                    apakah_angka = False
                    break
        else:
            apakah_angka = False
        
        if apakah_angka:
            id_p = int(id_p_str)
            index_ketemu = -1
            for i in range(len(pelanggan_db)):
                if pelanggan_db[i][0] == id_p:
                    index_ketemu = i
                    break
            
            if index_ketemu > -1:
                p_lama = pelanggan_db[index_ketemu]
                print(f'Data lama -> Nama: {p_lama[1]}, HP: {p_lama[2]}')
                nama_baru = input('Masukkan nama baru (kosongkan jika tidak ingin diubah): ')
                hp_baru = input('Masukkan HP baru (kosongkan jika tidak ingin diubah): ')
                
                nama_update = p_lama[1]
                if nama_baru != "":
                    nama_update = nama_baru
                    
                hp_update = p_lama[2]
                if hp_baru != "":
                    hp_update = hp_baru
                
                p_update = (p_lama[0], nama_update, hp_update)
                pelanggan_db[index_ketemu] = p_update
                print(f'\nBerhasil. Data pelanggan ID {id_p} telah diubah.')
            else:
                print(f'Gagal. Pelanggan dengan ID {id_p} tidak ditemukan.')
        else:
            print('Gagal. ID Pelanggan harus berupa angka.')

    elif pilihan == '10':
        print('\n--- [10] Hapus Suku Cadang dari Stok ---')
        id_sc_str = input('Masukkan ID barang yang akan dihapus: ')
        
        apakah_angka = True
        if len(id_sc_str) > 0:
            for karakter in id_sc_str:
                if karakter not in '0123456789':
                    apakah_angka = False
                    break
        else:
            apakah_angka = False

        if apakah_angka:
            id_sc = int(id_sc_str)
            index_ketemu = -1
            for i in range(len(sukucadang_db)):
                if sukucadang_db[i][0] == id_sc:
                    index_ketemu = i
                    break
            
            if index_ketemu > -1:
                sukucadang_db.pop(index_ketemu)
                print(f'\nBerhasil. Barang dengan ID {id_sc} sudah dihapus.')
            else:
                print(f'Gagal. Barang dengan ID {id_sc} tidak ditemukan.')
        else:
            print('Gagal. ID Barang harus berupa angka.')

    elif pilihan == '11':
        print('\n--- [11] Hapus (Batalkan) Work Order ---')
        id_wo_str = input('Masukkan ID Work Order yang akan dihapus: ')

        apakah_angka = True
        if len(id_wo_str) > 0:
            for karakter in id_wo_str:
                if karakter not in '0123456789':
                    apakah_angka = False
                    break
        else:
            apakah_angka = False

        if apakah_angka:
            id_wo = int(id_wo_str)
            index_ketemu = -1
            for i in range(len(workorder_db)):
                if workorder_db[i][0] == id_wo:
                    index_ketemu = i
                    break
            
            if index_ketemu > -1:
                workorder_db.pop(index_ketemu)
                print(f'\nBerhasil. Work Order ID {id_wo} sudah dibatalkan.')
            else:
                print(f'Gagal. Work Order dengan ID {id_wo} tidak ditemukan.')
        else:
            print('Gagal. ID Work Order harus berupa angka.')

    elif pilihan == '0':
        program_jalan = False
        print('\nTerima kasih telah menggunakan aplikasi ini.')
    else:
        print('\nPilihan tidak valid. Silakan masukkan nomor yang ada di menu.')