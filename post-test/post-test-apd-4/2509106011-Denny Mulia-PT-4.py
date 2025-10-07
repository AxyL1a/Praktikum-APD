belanja_lagi = 'ya'
while belanja_lagi == 'ya':
    print('SELAMAT DATANG DI PET SHOP THOMAS_TzY\n')
    makanan_kucing = 'Makanan Kucing'
    harga1 = 50000
    makanan_anjing = 'Makanan Anjing'
    harga2 = 60000
    vitamin_hewan = 'Vitamin Hewan'
    harga3 = 30000
    struk_belanja = ''
    total_belanja = 0
    diskon = 0
    jawaban_member = input('Apakah anda member? (ya/tidak): ')
    if jawaban_member == 'ya':
        print('\nSILAHKAN LOGIN!')
        nama_terdaftar = 'Denny'
        password_terdaftar = '011'
        kesempatan = 3
        for i in range(kesempatan):
            nama = input('Masukkan nama anda: ')
            password = input('Masukkan password anda: ')
            if nama == nama_terdaftar and password == password_terdaftar:
                print('LOGIN BERHASIL! Anda mendapatkan diskon 15% karena sebagai member')
                diskon = 0.15
                break
            else:
                sisa_kesempatan = kesempatan - (i + 1)
                if sisa_kesempatan > 0:
                    print(f'Login gagal, kesempatan login anda tersisa {sisa_kesempatan}')
                else:
                    print('Login gagal. Anda bukan sebagai member')
    while True:
        print('\nSilakan pilih produk')
        print(f'1. {makanan_kucing} - Rp.{harga1}')
        print(f'2. {makanan_anjing} - Rp.{harga2}')
        print(f'3. {vitamin_hewan} - Rp.{harga3}')
        print('4. Selesai belanja')
        pilihan = int(input('Masukkan pilihan produk (1-4): '))
        if 1 <= pilihan <= 3:
            jumlah = int(input('Masukkan jumlah: '))
            if jumlah > 0:
                if pilihan == 1:
                    nama_produk = makanan_kucing
                    harga_produk = harga1
                elif pilihan == 2:
                    nama_produk = makanan_anjing
                    harga_produk = harga2
                elif pilihan == 3:
                    nama_produk = vitamin_hewan
                    harga_produk = harga3
                total = harga_produk * jumlah
                total_belanja = total_belanja + total
                baris_struk = f'{nama_produk}, Jumlah: {jumlah}, total: Rp.{total}\n'
                struk_belanja = struk_belanja + baris_struk
                print(f'Berhasil menambahkan {jumlah} {nama_produk}')
                print(f'Total belanja : Rp.{total_belanja}')
            else:
                print('Jumlah harus lebih dari 0')
        elif pilihan == 4:
            if total_belanja == 0:
                print('Anda belum membeli apapun')
            else:
                break
        else:
            print('Pilihan tidak ada')
    if total_belanja > 0:
        print('-'*50)
        print('               STRUK PEMBAYARAN')
        print('-'*50)
        print(struk_belanja)
        if diskon > 0:
            jumlah_diskon = total_belanja * diskon
            total_bayar = total_belanja - jumlah_diskon
            print(f'Total Harga        : Rp.{total_belanja}')
            print(f'Diskon Member (15%): Rp.{int(jumlah_diskon)}')
            print(f'Total Bayar        : Rp.{int(total_bayar)}')
        else:
            print(f'Total Bayar        : Rp.{total_belanja}')
    print('-'*50)
    print('         TERIMA KASIH SUDAH BERBELANJA')
    print('-'*50)
    belanja_lagi = input('Ingin membeli lagi? (ya/tidak): ')