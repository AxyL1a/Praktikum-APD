from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City"]
table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "Los Angeles"])

print(table)
# angka = max(3,4,9)
# print(angka)

# x = 42
# def fungsi():
#     x = 10
#     y = 20
#     z = 30
#     print(globals()['x'])
#     print(locals()['x'])
#     print(locals())
# fungsi()

# import math
# print(math.sqrt(16))
# print(math.factorial(4))

# import random
# print(random.randint(1, 5)) 
# pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apcb"
# print(random.choice(pilih_acak)) 
# print(random.choice(acak)) 
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)
# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) 
# print(acak_kartu)

# import inquirer

# # Buat pertanyaan dengan pilihan yang bisa dipilih pakai panah
# pertanyaan = [
#     inquirer.List(
#         'bahasa',
#         message="Pilih bahasa pemrograman favoritmu:",
#         choices=['Python', 'JavaScript', 'Java', 'C++', 'Go']
#     )
# ]

# # Jalankan pertanyaan
# jawaban = inquirer.prompt(pertanyaan)

# # Tampilkan hasil
# print(f"\nKamu memilih: {jawaban['bahasa']} ✨")

import necessaryFunction as nf


def main():
    while True:
        load()
        mood = input('\nBagaimana Mood kalian hari ini?(ketik 0 jika ingin keluar) ')
        print(mood)
        delayInput()
        clear()
        if mood == '0':
            return False

if __name__ == "__main__":
    main()