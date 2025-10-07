# ulangi = 10
# for i in range (ulangi):
#     print(f'perulangan ke {i}')

# for i in range(1, 10):
#     if i % 2 != 0:
#         print(f"Angka genap ditemukan: {i}")
# print("\nProgram selesai.")

# for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
# print('') #biar ada jarak tiap iterasi

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
# print(f"Total perulangan: {hitung}")

#segitiga siku siku
# tinggi = 10
# for i in range (tinggi):
#     print('*' * (i))

# angka = [2, 5, 8, 12, 15, 7, 20]
# print("Mencari angka pertama yang lebih besar dari 10...")
# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
# print(f"Angka genap ditemukan: {i}")
# print("\nProgram selesai.")
nama_terdaftar = 'Denny'
password_terdaftar = '011'
kesempatan = 3
for _ in range(kesempatan):
    nama = input (f'masukkan nama anda: ')
    password = input (f'masukkan password anda: ')
    berhasil = nama_terdaftar == nama and password_terdaftar == password
    if berhasil:
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
            print('Pilihan tidak ada')
        total_harga = harga * jumlah
        diskon = total_harga * 0.15 
        total_bayar = total_harga - diskon
        print('\n' + '=' * 49)
        print(f'|   Total harga sebelum diskon  : Rp {total_harga}{' ':<5}|')
        print(f'|   Diskon (15%)                : Rp {diskon}{' ':<4}|')
        print(f'|   Total yang harus dibayar    : Rp {total_bayar}{' ':<3}|')
        break
    else:
        print(f'login gagal, kesempatan login anda tersisa {kesempatan - (_ + 1)}')
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
    print('Pilihan tidak ada')
total_harga = harga * jumlah
print(f'Total yang harus dibayar    : Rp {total_harga}')
