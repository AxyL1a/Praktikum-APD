
from data import *
from tampilan_menu import *
from masuk_daftar import *
from proses_program import *
from tahap_input import *
def main():
    user_login = None
    program_berjalan = True
    print(f"--- Aplikasi Servis Kendaraan ---")
    while program_berjalan:
        while user_login is None and program_berjalan:
            tampil_menu_awal()
            menu_awal = input('Masukkan pilihan Anda: ')
            if menu_awal == '1':
                user_login = proses_login()
            elif menu_awal == '2':
                registrasi_user_baru()
            elif menu_awal == '0':
                program_berjalan = False
                break
            else:
                print('\nPilihan tidak valid.')
                input('Tekan Enter untuk melanjutkan...')
        while user_login and program_berjalan:
            tampil_menu_utama(user_login)
            menu_utama = input('Masukkan pilihan Anda: ')
            if menu_utama == '4':
                lihat_riwayat()
            elif menu_utama == '5':
                lihat_stok()
            elif menu_utama == '6':
                lihat_servis_aktif()
            elif menu_utama == '0':
                user_login = logout(user_login)
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
                    input('Tekan Enter untuk melanjutkan...')
            else:
                if menu_utama not in ['4', '5', '6', '0']:
                    print('\nPilihan tidak valid atau Anda tidak memiliki hak akses.')
                    input('Tekan Enter untuk melanjutkan...')
    print('\nTerima kasih telah menggunakan aplikasi ini.')
if __name__ == "__main__":
    main()