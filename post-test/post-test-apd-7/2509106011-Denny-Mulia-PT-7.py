import os

data_user = {
    'Denny': {'password': '011', 'role': 'admin'},
    'Pedro': {'password': '078', 'role': 'pengguna'}
}
data_pelanggan = {}
data_stok = {}
data_servis = {}

id_pelanggan_baru = 1
id_servis_baru = 1
user_login = None
program_berjalan = True

def hapus():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampil_menu_awal():
    hapus()
    print('==============================================')
    print('        PROGRAM SERVIS KENDARAAN        ')
    print('==============================================')
    print('\n1. Login')
    print('2. Register')
    print('0. Keluar Aplikasi')

def validasi_login(username, password):
    user = data_user.get(username) 
    if user and user['password'] == password:
        return user
    else:
        return None

def cek_servis_aktif(nopol):
    for servis in data_servis.values():
        if servis['nopol'] == nopol and servis['status'] == 'Dikerjakan':
            return True
    return False

def input_angka(pesan):
    input_pesan = input(pesan)
    
    if input_pesan.isdigit():
        return input_pesan
    else:
        print("Input tidak valid. Harap masukkan angka saja.")
        return input_angka(pesan) 

def registrasi_user_baru():
    global data_user
    hapus()
    print('--- [ REGISTER PENGGUNA BARU ] ---')
    
    username_baru = input('Masukkan username baru: ')
    
    if username_baru in data_user:
        print(f'\nGagal. Username "{username_baru}" sudah ada. Silakan coba lagi.')
    else:
        password_baru = input('Masukkan password baru: ')
        role_baru = ''
        while role_baru not in ['admin', 'pengguna']:
            role_baru = input('Pilih peran (admin / pengguna): ').lower()
            if role_baru not in ['admin', 'pengguna']:
                print('Peran tidak valid. Harap pilih "admin" atau "pengguna".')
        
        data_user[username_baru] = {'password': password_baru, 'role': role_baru}
        print(f'\nBerhasil. Pengguna "{username_baru}" telah terdaftar.')
    input('Tekan Enter untuk kembali...')

def proses_login():
    global user_login 
    hapus()
    print('--- [ LOGIN ] ---')
    
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')

    hasil_login = validasi_login(username, password)
    
    if hasil_login:
        user_login = {'username': username, 'role': hasil_login['role']}
        print(f'\nLogin berhasil. Selamat datang, {username} ({user_login["role"]})!')
        input('Tekan Enter untuk masuk ke menu utama...')
    else:
        print('\nGagal. Username atau password salah.')
        input('Tekan Enter untuk mencoba lagi...')

def tampil_menu_utama():
    hapus()
    if user_login:
        print(f"User: {user_login['username']} | Peran: {user_login['role']}")
    print('\n========= MENU UTAMA =========')
    
    print('\n--- LIHAT DATA ---')
    print('4. Lihat Riwayat Servis Kendaraan')
    print('5. Lihat Stok Suku Cadang')
    print('6. Lihat Kendaraan yang Sedang Dikerjakan')
    
    if user_login and user_login['role'] == 'admin':
        print('\n--- INPUT DATA ---')
        print('1. Tambah Pelanggan Baru')
        print('2. Buat Servis Baru')
        print('3. Tambah Stok Suku Cadang')
        print('\n--- UBAH DATA ---')
        print('7. Ubah Status Servis')
        print('8. Tambah Catatan Servis')
        print('9. Ubah Data Pelanggan')
        print('\n--- HAPUS DATA ---')
        print('10. Hapus Suku Cadang')
        print('11. Hapus (Batalkan) Servis')
        
    print('\n0. LOGOUT')

def tambah_pelanggan():
    global data_pelanggan, id_pelanggan_baru
    print('\n--- [1] Tambah Pelanggan Baru ---')
    nama = input('Masukkan nama pelanggan: ')
    no_hp = input_angka('Masukkan nomor hp: ')
    
    id_baru = str(id_pelanggan_baru)
    data_pelanggan[id_baru] = {'Nama': nama, 'Nomor hp': no_hp}
    
    print(f'\nBerhasil. Pelanggan "{nama}" telah disimpan dengan ID {id_baru}.')
    id_pelanggan_baru += 1

def buat_servis_baru():
    global data_servis, id_servis_baru
    print('\n--- [2] Buat Servis Baru ---')

    if not data_pelanggan:
        print('Belum ada data pelanggan. Silakan tambah pelanggan dulu.')
        return 

    id_pelanggan = input_angka('Masukkan ID pelanggan: ')
    
    if id_pelanggan not in data_pelanggan:
        print(f'Gagal. Pelanggan dengan ID {id_pelanggan} tidak ditemukan.')
    else:
        nopol = input('Masukkan nomor polisi kendaraan: ').upper()
        
        if cek_servis_aktif(nopol):
            print(f'Gagal. Kendaraan {nopol} statusnya sudah "Dikerjakan".')
        else:
            id_baru = str(id_servis_baru)
            data_servis[id_baru] = {'id_pelanggan': id_pelanggan, 'nopol': nopol, 'status': 'Dikerjakan', 'catatan': ''}
            print(f'\nBerhasil. Servis (ID: {id_baru}) untuk {nopol} telah dibuat.')
            id_servis_baru += 1

def tambah_stok():
    global data_stok
    print('\n--- [3] Tambah Stok Suku Cadang ---')
    
    id_barang = input_angka('Masukkan ID barang (angka): ')
    
    if id_barang in data_stok:
        print(f'Gagal. ID barang {id_barang} sudah digunakan.')
    else:
        nama_barang = input('Masukkan nama barang: ')
        stok_input = input_angka('Masukkan jumlah stok: ')
        
        stok = int(stok_input)
        if stok < 0:
            print('Gagal. Stok tidak boleh negatif.')
        else:
            data_stok[id_barang] = {'nama_barang': nama_barang, 'stok': stok}
            print(f'\nBerhasil. Barang "{nama_barang}" (ID: {id_barang}) sudah ditambahkan.')

def lihat_riwayat():
    print('\n--- [4] Lihat Riwayat Servis Kendaraan ---')
    nopol = input('Masukkan nomor polisi: ').upper()
    
    ada_riwayat = False
    print(f'\n--- Hasil Pencarian untuk {nopol} ---')
    for id_servis, data in data_servis.items():
        if data['nopol'] == nopol:
            id_pelanggan = data['id_pelanggan']
            nama = data_pelanggan.get(id_pelanggan, {'Nama': 'Tidak Diketahui'})['Nama']
            print(f"ID Servis: {id_servis}, Pelanggan: {nama}, Status: {data['status']}, Catatan: {data['catatan']}")
            ada_riwayat = True
    
    if not ada_riwayat:
        print(f'Tidak ada riwayat servis untuk kendaraan {nopol}.')

def lihat_stok():
    print('\n--- [5] Lihat Stok Suku Cadang ---')
    if not data_stok:
        print('Stok suku cadang masih kosong.')
    else:
        print('ID | Nama Barang      | Stok')
        print('--------------------------------')
        for id_stok, data in data_stok.items():
            print(f"{id_stok:<2} | {data['nama_barang']:<16} | {data['stok']}")

def lihat_servis_aktif():
    print('\n--- [6] Lihat Kendaraan yang Sedang Dikerjakan ---')
    ada_yang_dikerjakan = False
    for id_servis, data in data_servis.items():
        if data['status'] == 'Dikerjakan':
            print(f"ID Servis: {id_servis}, Nopol: {data['nopol']}, Status: {data['status']}")
            ada_yang_dikerjakan = True
    
    if not ada_yang_dikerjakan:
        print('Saat ini tidak ada kendaraan yang sedang dikerjakan.')

def ubah_status_servis():
    global data_servis
    print('\n--- [7] Ubah Status Servis ---')
    id_servis = input_angka('Masukkan ID Servis yang akan diubah: ')
    
    if id_servis not in data_servis:
        print(f'Gagal. Servis dengan ID {id_servis} tidak ditemukan.')
    else:
        status_lama = data_servis[id_servis]['status']
        print(f'Status saat ini untuk ID {id_servis} adalah "{status_lama}"')
        status_baru = input('Masukkan status baru: ')
        data_servis[id_servis]['status'] = status_baru
        print(f'\nBerhasil. Status ID {id_servis} telah diubah menjadi "{status_baru}".')

def tambah_catatan_servis():
    global data_servis
    print('\n--- [8] Tambah Catatan Servis ---')
    id_servis = input_angka('Masukkan ID Servis: ')

    if id_servis not in data_servis:
        print(f'Gagal. Servis dengan ID {id_servis} tidak ditemukan.')
    else:
        catatan_baru = input('Tulis catatan dari montir: ')
        catatan_lama = data_servis[id_servis].get('catatan', '')
        
        if catatan_lama:
            data_servis[id_servis]['catatan'] = f"{catatan_lama} | {catatan_baru}"
        else:
            data_servis[id_servis]['catatan'] = catatan_baru
        print(f'\nBerhasil. Catatan untuk ID {id_servis} sudah disimpan.')

def ubah_data_pelanggan():
    global data_pelanggan
    print('\n--- [9] Ubah Data Pelanggan ---')
    id_pelanggan = input_angka('Masukkan ID pelanggan yang akan diubah: ')
    
    if id_pelanggan not in data_pelanggan:
        print(f'Gagal. Pelanggan dengan ID {id_pelanggan} tidak ditemukan.')
    else:
        data_lama = data_pelanggan[id_pelanggan]
        print(f'Data lama -> Nama: {data_lama["Nama"]}, Nomor hp: {data_lama["Nomor hp"]}')
        nama_baru = input('Masukkan nama baru (kosongkan jika tidak diubah): ')
        no_hp_baru = input('Masukkan Nomor hp baru (kosongkan jika tidak diubah): ')
        
        if nama_baru: 
            data_pelanggan[id_pelanggan]['Nama'] = nama_baru
        if no_hp_baru:
            if no_hp_baru.isdigit():
                data_pelanggan[id_pelanggan]['Nomor hp'] = no_hp_baru
            elif no_hp_baru:
                print("Nomor hp baru tidak valid (harus angka), tidak diubah.")
                
        print(f'\nBerhasil. Data pelanggan ID {id_pelanggan} telah diubah.')

def hapus_stok():
    global data_stok
    print('\n--- [10] Hapus Suku Cadang ---')
    id_barang = input_angka('Masukkan ID barang yang akan dihapus: ')
    
    if id_barang not in data_stok:
        print(f'Gagal. Barang dengan ID {id_barang} tidak ditemukan.')
    else:
        barang_dihapus = data_stok.pop(id_barang)
        print(f'\nBerhasil. Barang "{barang_dihapus["nama_barang"]}" sudah dihapus.')

def hapus_servis():
    global data_servis
    print('\n--- [11] Hapus (Batalkan) Servis ---')
    id_servis = input_angka('Masukkan ID Servis yang akan dihapus: ')

    if id_servis not in data_servis:
        print(f'Gagal. Servis dengan ID {id_servis} tidak ditemukan.')
    else:
        data_servis.pop(id_servis)
        print(f'\nBerhasil. Servis ID {id_servis} sudah dibatalkan.')

def logout():
    global user_login
    print(f'\nPengguna "{user_login["username"]}" telah logout.')
    user_login = None


while program_berjalan:

    while user_login is None and program_berjalan:
        tampil_menu_awal() 
        menu_awal = input('Masukkan pilihan Anda: ')

        if menu_awal == '1':
            proses_login()
        elif menu_awal == '2':
            registrasi_user_baru() 
        elif menu_awal == '0':
            program_berjalan = False
        else:
            print('\nPilihan tidak valid.')
            input('Tekan Enter untuk melanjutkan...')

    while user_login:
        tampil_menu_utama() 
        menu_utama = input('Masukkan pilihan Anda: ')
        
        if menu_utama == '4':
            lihat_riwayat()
        elif menu_utama == '5':
            lihat_stok() 
        elif menu_utama == '6':
            lihat_servis_aktif()
        elif menu_utama == '0':
            logout() 
            
        elif user_login['role'] == 'admin':
            if menu_utama == '1':
                tambah_pelanggan()
            elif menu_utama == '2':
                buat_servis_baru()
            elif menu_utama == '3':
                tambah_stok()
            elif menu_utama == '7':
                ubah_status_servis()
            elif menu_utama == '8':
                tambah_catatan_servis()
            elif menu_utama == '9':
                ubah_data_pelanggan()
            elif menu_utama == '10':
                hapus_stok()
            elif menu_utama == '11':
                hapus_servis()
            else:
                print('\nPilihan tidak valid.')
        
        else: 
            if menu_utama not in ['4', '5', '6', '0']:
                print('\nPilihan tidak valid atau Anda tidak memiliki hak akses.')
        
        if user_login:
            input('\nTekan Enter untuk kembali ke menu...')

print('\nTerima kasih telah menggunakan aplikasi ini.')