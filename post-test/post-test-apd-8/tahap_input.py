import os
def hapus():
    os.system('cls' if os.name == 'nt' else 'clear')
def input_angka(pesan):
    input_pesan = input(pesan)
    if input_pesan.isdigit():
        return input_pesan
    else:
        print("Input tidak valid. Harap masukkan angka saja.")
        return input_angka(pesan)