print('=' * 49)
print('|     SELAMAT DATANG DI PET SHOP THOMAS_TzY     |')
print('=' * 49)
status_member = input('apakah anda member (ya/tidak)? ').lower()
if status_member == 'ya':
    print('=' * 49)
    print('|'+ ' ' * 16 + 'SILAHKAN LOGIN!' + ' ' * 16 + '|')
    print('=' * 49)
    nama_terdaftar = 'Denny'
    password_terdaftar = '011'
    input_nama = input('Masukkan nama: ')
    input_password = input('Masukkan password: ')
    login_berhasil =  True if input_nama == nama_terdaftar and input_password == password_terdaftar else False 
    if login_berhasil:
        print('LOGIN BERHASIL!, SELAMAT DATANG DI PET SHOP THOMAS_TzY')
        print('silakana pilih produk yang ingin dibeli')
        print('1. Makanan Kucing - Rp 50.000')
        print('2. Makanan Anjing - Rp 60.000')
        print('3. Vitamin Hewan - Rp 30.000')
        pilihan = int(input('Masukkan pilihan (1/2/3): '))
        jumlah = int(input('Masukkan jumlah: '))
        if pilihan == 1:
            harga = 50000
            produk = 'Makanan Kucing'
        elif pilihan == 2:
            harga = 60000
            produk = 'Makanan Anjing'
        elif pilihan == 3:
            harga = 30000
            produk = 'Vitamin Hewan'
        else:
            print('Pilihan tidak valid.')
            exit()
        total_harga = harga * jumlah
        diskon = total_harga * 0.15 
        total_bayar = total_harga - diskon
        print('\n' + '=' * 49)
        print(f'|   Total harga sebelum diskon  : Rp {total_harga}{' ':<5}|')
        print(f'|   Diskon (15%)                : Rp {diskon}{' ':<4}|')
        print(f'|   Total yang harus dibayar    : Rp {total_bayar}{' ':<3}|')
    else:
        print('Login gagal! silahkan coba lagi')
        exit()
elif status_member == 'tidak':
    print('SELAMAT DATANG DI PET SHOP THOMAS_TzY')
    print('silakan pilih produk yang ingin dibeli')
    print('1. Makanan Kucing - Rp 50.000')
    print('2. Makanan Anjing - Rp 60.000')
    print('3. Vitamin Hewan - Rp 30.000')
    pilihan = int(input('Masukkan pilihan (1/2/3): '))
    jumlah = int(input('Masukkan jumlah: '))
    if pilihan == 1:
        harga = 50000
        produk = 'Makanan Kucing'
    elif pilihan == 2:
        harga = 60000
        produk = 'Makanan Anjing'
    elif pilihan == 3:
        harga = 30000
        produk = 'Vitamin Hewan'
    else:
        print('Pilihan tidak valid.')
        exit()
    total_harga = harga * jumlah
    print('=' * 49)
    print(f'|   Total yang harus dibayar    : Rp {total_harga}{' ':<5}|')
print('=' * 49)
print('|         TERIMA KASIH SUDAH BERBELANJA         |')
print('=' * 49)