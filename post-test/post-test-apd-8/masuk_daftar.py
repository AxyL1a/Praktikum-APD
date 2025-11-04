from data import *
from tahap_input import *
def validasi_login(username, password):
    user = data_user.get(username)
    if user and user['password'] == password:
        return user
    else:
        return None
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
        print(f'\nBerhasil. Pengguna "{username_baru}" dengan peran "{role_baru}" telah terdaftar.')
    input('Tekan Enter untuk kembali...')
def proses_login():
    hapus()
    print('--- [ LOGIN ] ---')
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    hasil_login = validasi_login(username, password)
    if hasil_login:
        print(f'\nLogin berhasil. Selamat datang, {username} ({hasil_login["role"]})!')
        input('Tekan Enter untuk masuk ke menu utama...')
        return {'username': username, 'role': hasil_login['role']}
    else:
        print('\nGagal. Username atau password salah.')
        input('Tekan Enter untuk mencoba lagi...')
        return None