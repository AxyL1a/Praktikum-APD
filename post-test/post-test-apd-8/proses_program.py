from data import *
from tahap_input import *
from prettytable import *
def cek_servis_aktif(nopol):
    for servis in data_servis.values():
        if servis['nopol'] == nopol and servis['status'] == 'Dikerjakan':
            return True
    return False

def tambah_pelanggan():
    global id_pelanggan_baru
    print('\n--- [1] Tambah Pelanggan Baru ---')
    nama = input('Masukkan nama pelanggan: ')
    no_hp = input_angka('Masukkan nomor hp: ')
    id_baru = str(id_pelanggan_baru)
    data_pelanggan[id_baru] = {'Nama': nama, 'Nomor hp': no_hp}
    print(f'\nBerhasil. Pelanggan "{nama}" telah disimpan dengan ID {id_baru}.')
    id_pelanggan_baru += 1
    input('Tekan Enter untuk kembali...')

def buat_servis_baru():
    global id_servis_baru
    print('\n--- [2] Buat Work Order (WO) Baru ---')
    if not data_pelanggan:
        print('Belum ada data pelanggan. Silakan tambah pelanggan dulu.')
        input('Tekan Enter untuk kembali...')
        return
    id_pelanggan = input_angka('Masukkan ID pelanggan: ')
    if id_pelanggan not in data_pelanggan:
        print(f'Gagal. Pelanggan dengan ID {id_pelanggan} tidak ditemukan.')
        input('Tekan Enter untuk kembali...')
        return
    else:
        nopol = input('Masukkan nomor polisi kendaraan: ').upper()
        if cek_servis_aktif(nopol):
            print(f'Gagal. Kendaraan {nopol} statusnya sudah "Dikerjakan".')
            input('Tekan Enter untuk kembali...')
            return
        else:
            id_baru = str(id_servis_baru)
            data_servis[id_baru] = {'id_pelanggan': id_pelanggan, 'nopol': nopol, 'status': 'Dikerjakan', 'catatan': ''}
            print(f'\nBerhasil. Work Order (ID: {id_baru}) untuk {nopol} telah dibuat.')
            id_servis_baru += 1
            input('Tekan Enter untuk kembali...')

def tambah_stok():
    print('\n--- [3] Tambah Suku Cadang ke Stok ---')
    id_barang = input_angka('Masukkan ID barang (angka): ')
    if id_barang in data_stok:
        print(f'Gagal. ID barang {id_barang} sudah digunakan.')
        input('Tekan Enter untuk kembali...')
        return
    else:
        nama_barang = input('Masukkan nama barang: ')
        stok_input = input_angka('Masukkan jumlah stok: ')
        stok = int(stok_input)
        if stok < 0:
            print('Gagal. Stok tidak boleh negatif.')
            input('Tekan Enter untuk kembali...')
            return
        else:
            data_stok[id_barang] = {'nama_barang': nama_barang, 'stok': stok}
            print(f'\nBerhasil. Barang "{nama_barang}" (ID: {id_barang}) sudah ditambahkan.')
            input('Tekan Enter untuk kembali...')

def lihat_riwayat():
    print('\n--- [4] Lihat Riwayat Servis Kendaraan ---')
    nopol = input('Masukkan nomor polisi: ').upper()
    table = PrettyTable()
    table.field_names = ["ID Servis", "Pelanggan", "Status", "Catatan"]
    ada_riwayat = False
    for id_servis, data in data_servis.items():
        if data['nopol'] == nopol:
            id_pelanggan = data['id_pelanggan']
            nama = data_pelanggan.get(id_pelanggan, {'Nama': 'Tidak Diketahui'})['Nama']
            table.add_row([id_servis, nama, data['status'], data['catatan']])
            ada_riwayat = True
    print(f'\n--- Hasil Pencarian untuk {nopol} ---')
    if ada_riwayat:
        print(table)
    else:
        print(f'Tidak ada riwayat servis untuk kendaraan {nopol}.')
    input('Tekan Enter untuk kembali...')
    
def lihat_stok():
    print('\n--- [5] Lihat Stok Suku Cadang ---')
    table = PrettyTable()
    table.field_names = ["ID", "Nama Barang", "Stok"]
    if data_stok:
        for id_stok, data in data_stok.items():
            table.add_row([id_stok, data['nama_barang'], data['stok']])
        print(table)
    else:
        print('Stok suku cadang masih kosong.')
    input('Tekan Enter untuk kembali...')

def lihat_servis_aktif():
    print('\n--- [6] Lihat Kendaraan yang Sedang Dikerjakan ---')
    table = PrettyTable()
    table.field_names = ["ID Servis", "Nopol", "Status"]
    ada_yang_dikerjakan = False
    for id_servis, data in data_servis.items():
        if data['status'] == 'Dikerjakan':
            table.add_row([id_servis, data['nopol'], data['status']])
            ada_yang_dikerjakan = True
    if ada_yang_dikerjakan:
        print(table)
    else:
        print('Saat ini tidak ada kendaraan yang sedang dikerjakan.')
    input('Tekan Enter untuk kembali...')

def ubah_status_servis():
    print('\n--- [7] Ubah Status Work Order ---')
    id_servis = input_angka('Masukkan ID Work Order yang akan diubah: ')
    if id_servis not in data_servis:
        print(f'Gagal. Work Order dengan ID {id_servis} tidak ditemukan.')
        input('Tekan Enter untuk kembali...')
        return
    else:
        status_lama = data_servis[id_servis]['status']
        print(f'Status saat ini untuk ID {id_servis} adalah "{status_lama}"')
        status_baru = input('Masukkan status baru: ')
        data_servis[id_servis]['status'] = status_baru
        print(f'\nBerhasil. Status ID {id_servis} telah diubah menjadi "{status_baru}".')
        input('Tekan Enter untuk kembali...')

def tambah_catatan_servis():
    print('\n--- [8] Tambah Catatan untuk Work Order ---')
    id_servis = input_angka('Masukkan ID Servis: ')
    if id_servis not in data_servis:
        print(f'Gagal. Servis dengan ID {id_servis} tidak ditemukan.')
        input('Tekan Enter untuk kembali...')
        return
    else:
        catatan_baru = input('Tulis catatan dari montir: ')
        catatan_lama = data_servis[id_servis].get('catatan', '')
        if catatan_lama:
            data_servis[id_servis]['catatan'] = f"{catatan_lama} | {catatan_baru}"
        else:
            data_servis[id_servis]['catatan'] = catatan_baru
        print(f'\nBerhasil. Catatan untuk ID {id_servis} sudah disimpan.')
        input('Tekan Enter untuk kembali...')

def ubah_data_pelanggan():
    print('\n--- [9] Ubah Data Pelanggan ---')
    id_pelanggan = input_angka('Masukkan ID pelanggan yang akan diubah: ')
    if id_pelanggan not in data_pelanggan:
        print(f'Gagal. Pelanggan dengan ID {id_pelanggan} tidak ditemukan.')
        input('Tekan Enter untuk kembali...')
        return
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
        input('Tekan Enter untuk kembali...')

def hapus_stok():
    print('\n--- [10] Hapus Suku Cadang ---')
    id_barang = input_angka('Masukkan ID barang yang akan dihapus: ')
    if id_barang not in data_stok:
        print(f'Gagal. Barang dengan ID {id_barang} tidak ditemukan.')
        input('Tekan Enter untuk kembali...')
        return
    else:
        barang_dihapus = data_stok.pop(id_barang)
        print(f'\nBerhasil. Barang "{barang_dihapus["nama_barang"]}" sudah dihapus.')
        input('Tekan Enter untuk kembali...')

def hapus_servis():
    print('\n--- [11] Hapus (Batalkan) Servis ---')
    id_servis = input_angka('Masukkan ID Servis yang akan dihapus: ')
    if id_servis not in data_servis:
        print(f'Gagal. Servis dengan ID {id_servis} tidak ditemukan.')
        input('Tekan Enter untuk kembali...')
        return
    else:
        data_servis.pop(id_servis)
        print(f'\nBerhasil. Servis ID {id_servis} sudah dibatalkan.')
        input('Tekan Enter untuk kembali...')

def logout(user_login):
    print(f'\nPengguna "{user_login["username"]}" telah logout.')
    input('Tekan Enter untuk kembali ke menu awal...')
    return None