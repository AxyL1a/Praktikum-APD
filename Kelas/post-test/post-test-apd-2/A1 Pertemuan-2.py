nama_pasien = input("Masukkan Nama Pasien: ")
tinggi_badan = float(input("Masukkan Tinggi Badan (cm): "))
berat_badan = float(input("Masukkan Berat Badan (kg): "))
status_list = ["Berat Badan Ideal", "Kelebihan Berat Badan"]
berat_ideal = tinggi_badan - 100
kelebihan = berat_badan > berat_ideal
status = status_list[int(kelebihan)]
print("\n" + "-" * 57)
print(f"|{'HASIL CEK BERAT BADAN':^55}|")
print("-" * 57)
print(f"| Nama Pasien   : {nama_pasien:<36}  |")
print(f"| Tinggi Badan  : {tinggi_badan:.0f} cm{' ':<31} |")
print(f"| Berat Badan   : {berat_badan:.0f} kg{' ':<32} |")
print(f"| Berat Ideal   : {berat_ideal:.0f} kg{' ':<32} |")
print(f"| Status        : {status:<36}  |")
print("-" * 57)