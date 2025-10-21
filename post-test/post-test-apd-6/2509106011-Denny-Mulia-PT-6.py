import os
penggunaterdaftar = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'pengguna'}
}
pelanggan = {}
sukucadang = {}
workorder = {}
id_pelanggan_selanjutnya = 1
id_wo_selanjutnya = 1
pengguna_aktif = None  
program_jalan = True
while program_jalan:

    while pengguna_aktif is None and program_jalan:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('==============================================')
        print('         PROGRAM SERVIS KENDARAAN         ')
        print('==============================================')
        print('\n1. Login')
        print('2. Register')
        print('0. Keluar Aplikasi')
        pilihan_awal = input('Masukkan pilihan Anda: ')

        if pilihan_awal == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--- [ REGISTER PENGGUNA BARU ] ---')
            username = input('Masukkan username baru: ')
            
            if username in penggunaterdaftar:
                print(f'\nGagal. Username "{username}" sudah ada. Silakan coba lagi.')

            else:
                password = input('Masukkan password baru: ')
                role = ''
                while role not in ['admin', 'pengguna']:
                    role = input('Pilih peran (admin / pengguna): ').lower()
                    if role not in ['admin', 'pengguna']:
                        print('Peran tidak valid. Harap pilih "admin" atau "pengguna".')
                
                penggunaterdaftar[username] = {'password': password, 'role': role}
                print(f'\nBerhasil. Pengguna "{username}" dengan peran "{role}" telah terdaftar.')
            input('Tekan Enter untuk kembali...')

        elif pilihan_awal == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--- [ LOGIN ] ---')
            username = input('Masukkan username: ')
            password = input('Masukkan password: ')

            if username in penggunaterdaftar and penggunaterdaftar[username]['password'] == password:
                pengguna_aktif = {'username': username, 'role': penggunaterdaftar[username]['role']}
                print(f'\nLogin berhasil. Selamat datang, {username} ({pengguna_aktif["role"]})!')
                input('Tekan Enter untuk masuk ke menu utama...')

            else:
                print('\nGagal. Username atau password salah.')
                input('Tekan Enter untuk mencoba lagi...')

        elif pilihan_awal == '0':
            program_jalan = False
        
        else:
            print('\nPilihan tidak valid.')
            input('Tekan Enter untuk melanjutkan...')
    sesi_aktif = True

    if not program_jalan: 
        sesi_aktif = False

    while sesi_aktif:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"User: {pengguna_aktif['username']} | Peran: {pengguna_aktif['role']}")
        print('\n========= MENU UTAMA =========')
        
        is_admin = pengguna_aktif['role'] == 'admin'
        print('\n--- LIHAT DATA ---')
        print('4. Lihat Riwayat Servis Kendaraan')
        print('5. Lihat Stok Suku Cadang')
        print('6. Lihat Kendaraan yang Sedang Dikerjakan')
        if is_admin:
            print('\n--- INPUT DATA ---')
            print('1. Tambah Pelanggan Baru')
            print('2. Buat Work Order (WO) Baru')
            print('3. Tambah Suku Cadang ke Stok')
            print('\n--- UBAH DATA ---')
            print('7. Ubah Status Work Order')
            print('8. Tambah Catatan untuk Work Order')
            print('9. Ubah Data Pelanggan')
            print('\n--- HAPUS DATA ---')
            print('10. Hapus Suku Cadang dari Stok')
            print('11. Hapus (Batalkan) Work Order')
        print('\n0. LOGOUT')
        pilihan = input('Masukkan pilihan Anda: ')

        if pilihan == '1' and is_admin:
            print('\n--- [1] Tambah Pelanggan Baru ---')
            nama = input('Masukkan nama pelanggan: ')
            hp = input('Masukkan nomor HP: ')
            
            id_baru = str(id_pelanggan_selanjutnya)
            pelanggan[id_baru] = {'nama': nama, 'hp': hp}
            
            print(f'\nBerhasil. Pelanggan "{nama}" telah disimpan dengan ID {id_baru}.')
            id_pelanggan_selanjutnya += 1

        elif pilihan == '2' and is_admin:
            print('\n--- [2] Buat Work Order (WO) Baru ---')

            if not pelanggan:
                print('Belum ada data pelanggan. Silakan tambah pelanggan terlebih dahulu.')
            else:
                id_pelanggan = input('Masukkan ID pelanggan: ')
                
                if not id_pelanggan.isdigit() or id_pelanggan not in pelanggan:
                    print(f'Gagal. Pelanggan dengan ID {id_pelanggan} tidak ditemukan atau ID tidak valid.')
                else:
                    nopol = input('Masukkan nomor polisi kendaraan: ').upper()
                    
                    kendaraan_sedang_dikerjakan = False
                    for wo_data in workorder.values():
                        if wo_data['nopol'] == nopol and wo_data['status'] == 'Dikerjakan':
                            kendaraan_sedang_dikerjakan = True
                            break
                    
                    if kendaraan_sedang_dikerjakan:
                        print(f'Gagal. Kendaraan {nopol} statusnya sudah "Dikerjakan".')
                    else:
                        id_baru = str(id_wo_selanjutnya)
                        workorder[id_baru] = {'id_pelanggan': id_pelanggan, 'nopol': nopol, 'status': 'Dikerjakan', 'catatan': ''}
                        print(f'\nBerhasil. Work Order (ID: {id_baru}) untuk kendaraan {nopol} telah dibuat.')
                        id_wo_selanjutnya += 1
        elif pilihan == '3' and is_admin:
            print('\n--- [3] Tambah Suku Cadang ke Stok ---')
            id_barang_str = input('Masukkan ID barang (angka): ')
            nama_barang = input('Masukkan nama barang: ')
            stok_str = input('Masukkan jumlah stok: ')

            if not id_barang_str.isdigit() or not stok_str.isdigit():
                print('Gagal. ID barang dan stok harus berupa angka.')
            elif id_barang_str in sukucadang:
                print(f'Gagal. ID barang {id_barang_str} sudah digunakan.')
            else:
                sukucadang[id_barang_str] = {'nama_barang': nama_barang, 'stok': int(stok_str)}
                print(f'\nBerhasil. Barang "{nama_barang}" (ID: {id_barang_str}) sudah ditambahkan.')
        elif pilihan == '4':
            print('\n--- [4] Lihat Riwayat Servis Kendaraan ---')
            nopol = input('Masukkan nomor polisi: ').upper()
            
            ada_riwayat = False
            print(f'\n--- Hasil Pencarian untuk {nopol} ---')
            for wo_id, wo_data in workorder.items():
                if wo_data['nopol'] == nopol:
                    id_pelanggan = wo_data['id_pelanggan']
                    nama_pelanggan = pelanggan.get(id_pelanggan, {'nama': 'Tidak Diketahui'})['nama']
                    print(f"ID WO: {wo_id}, Pelanggan: {nama_pelanggan}, Status: {wo_data['status']}, Catatan: {wo_data['catatan']}")
                    ada_riwayat = True
            
            if not ada_riwayat:
                print(f'Tidak ada riwayat servis untuk kendaraan {nopol}.')
        elif pilihan == '5':
            print('\n--- [5] Lihat Stok Suku Cadang ---')
            if not sukucadang:
                print('Stok suku cadang masih kosong.')
            else:
                print('ID | Nama Barang      | Stok')
                print('--------------------------------')
                for sc_id, sc_data in sukucadang.items():
                    print(f"{sc_id:<2} | {sc_data['nama_barang']:<16} | {sc_data['stok']}")
        elif pilihan == '6':
            print('\n--- [6] Lihat Kendaraan yang Sedang Dikerjakan ---')
            ada_yang_dikerjakan = False
            for wo_id, wo_data in workorder.items():
                if wo_data['status'] == 'Dikerjakan':
                    print(f"ID WO: {wo_id}, Nopol: {wo_data['nopol']}, Status: {wo_data['status']}")
                    ada_yang_dikerjakan = True
            
            if not ada_yang_dikerjakan:
                print('Saat ini tidak ada kendaraan yang sedang dikerjakan.')
        elif pilihan == '7' and is_admin:
            print('\n--- [7] Ubah Status Work Order ---')
            id_wo_str = input('Masukkan ID Work Order yang akan diubah: ')
            
            if not id_wo_str.isdigit() or id_wo_str not in workorder:
                print(f'Gagal. Work Order dengan ID {id_wo_str} tidak ditemukan atau ID tidak valid.')
            else:
                wo_lama = workorder[id_wo_str]
                print(f'Status saat ini untuk WO ID {id_wo_str} adalah "{wo_lama["status"]}"')
                status_baru = input('Masukkan status baru: ')
                workorder[id_wo_str]['status'] = status_baru
                print(f'\nBerhasil. Status WO ID {id_wo_str} telah diubah menjadi "{status_baru}".')
        elif pilihan == '8' and is_admin:
            print('\n--- [8] Tambah Catatan untuk Work Order ---')
            id_wo_str = input('Masukkan ID Work Order: ')

            if not id_wo_str.isdigit() or id_wo_str not in workorder:
                print(f'Gagal. Work Order dengan ID {id_wo_str} tidak ditemukan atau ID tidak valid.')
            else:
                catatan_baru = input('Tulis catatan dari montir: ')
                workorder[id_wo_str]['catatan'] = catatan_baru
                print(f'\nBerhasil. Catatan untuk WO ID {id_wo_str} sudah disimpan.')
        elif pilihan == '9' and is_admin:
            print('\n--- [9] Ubah Data Pelanggan ---')
            id_p_str = input('Masukkan ID pelanggan yang akan diubah: ')
            
            if not id_p_str.isdigit() or id_p_str not in pelanggan:
                print(f'Gagal. Pelanggan dengan ID {id_p_str} tidak ditemukan atau ID tidak valid.')
            else:
                p_lama = pelanggan[id_p_str]
                print(f'Data lama -> Nama: {p_lama["nama"]}, HP: {p_lama["hp"]}')
                nama_baru = input('Masukkan nama baru (kosongkan jika tidak diubah): ')
                hp_baru = input('Masukkan HP baru (kosongkan jika tidak diubah): ')
                
                if nama_baru: pelanggan[id_p_str]['nama'] = nama_baru
                if hp_baru: pelanggan[id_p_str]['hp'] = hp_baru
                print(f'\nBerhasil. Data pelanggan ID {id_p_str} telah diubah.')
        elif pilihan == '10' and is_admin:
            print('\n--- [10] Hapus Suku Cadang dari Stok ---')
            id_sc_str = input('Masukkan ID barang yang akan dihapus: ')
            
            if not id_sc_str.isdigit() or id_sc_str not in sukucadang:
                print(f'Gagal. Barang dengan ID {id_sc_str} tidak ditemukan atau ID tidak valid.')
            else:
                del sukucadang[id_sc_str]
                print(f'\nBerhasil. Barang dengan ID {id_sc_str} sudah dihapus.')
        elif pilihan == '11' and is_admin:
            print('\n--- [11] Hapus (Batalkan) Work Order ---')
            id_wo_str = input('Masukkan ID Work Order yang akan dihapus: ')

            if not id_wo_str.isdigit() or id_wo_str not in workorder:
                print(f'Gagal. Work Order dengan ID {id_wo_str} tidak ditemukan atau ID tidak valid.')
            else:
                del workorder[id_wo_str]
                print(f'\nBerhasil. Work Order ID {id_wo_str} sudah dibatalkan.')
        elif pilihan == '0':
            print(f'\nPengguna "{pengguna_aktif["username"]}" telah logout.')
            pengguna_aktif = None
            sesi_aktif = False
        else:
            print('\nPilihan tidak valid atau Anda tidak memiliki hak akses untuk menu ini.')
        if sesi_aktif:
            input('\nTekan Enter untuk kembali ke menu...')
print('\nTerima kasih telah menggunakan aplikasi ini.')