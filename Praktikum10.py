# Tuple
# Nomer 1
# A
data_toples = ('Pardede Putra Anjasmara','2505060061','Teknologi Informasi')

# C
print(f'Nama : {data_toples[0]}')
print(f'NIM : {data_toples[1]}')
print(f'Jurusan : {data_toples[2]}')

# Dictionary
# Nomer 1
# A
keranjang = {    
    'apel':5000,
    'pisang':3000,
    'jeruk':7000,
    'anggur':15000
}

total_buah = 0
perulangan = ''
total_harga = 0
for cihuy,sibau in keranjang.items():
  # b
  total_buah += 1
  # c
  print("Harga", cihuy, ": Rp", sibau)
  # d
  total_harga += sibau
print(total_harga)