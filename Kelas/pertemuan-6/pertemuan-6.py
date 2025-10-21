# angka = [1,2,3,4,5,6,7,7,8]

# unik = set (angka)
# print(angka)

# daftar_buku ={
#     'buku1' : 'bumi manusia',
#     'buku2' : 'laut bercerita'
# }
# print (daftar_buku)
# print(daftar_buku['buku1'])

# Biodata = {
# 'Nama' : 'Denny Mulia',
# 'NIM' : 2509106011,
# 'KRS' : ['Pemrograman Web', 'Struktur Data', 'Basis Data'],
# 'Mahasiswa_Aktif' : True,
# 'Social Media' : {
# 'Instagram' : 'daffahrhap'
#     }
# }
# print(Biodata.get('Nama'))

# print (Biodata)
# for i, j in Biodata.items():
#     print(i)
#     print(j)
# print(f'nama saya adalah {Biodata['Nama']}')
# print(f'Instagram : {Biodata['Social Media']['Instagram']}')
# print(f'nama saya adalah {Biodata.get['Nama']}')
# print(Biodata.get('Nama'))
# print(Biodata.get('Nama'))
# print(Biodata.get('Alamat'))
# print(Biodata.get('Alamat', 'Key tersebut tidak ada'))

Film = {
'Avenger Endgame' : 'Action',
'Sherlock Holmes' : 'Mystery',
'The Conjuring' : 'Horror'
}


# #Sebelum Ditambah
# print(Film)
# Film['Zombieland'] = 'Comedy'
# Film.update({'Hours' : 'Thriller'})
# #Setelah Ditambah
# print(Film) 
# {
# 'Avenger Endgame': 'Action',
# 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror'
# }
# #Setelah Ditambah
# {'Avenger Endgame': 'Action',
# 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror',
# 'Zombieland': 'Comedy',
# 'Hours': 'Thriller'
# }

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])

# angka = {}
# print(type(angka))

# a = {10,11,12}
# b = {13,11,14}

# c = a | b
# print (c)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
#     print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

mahasiswa = [['a','b','c'],['d','e','f']]
for i in mahasiswa:
    # for j in i:
        print(i)