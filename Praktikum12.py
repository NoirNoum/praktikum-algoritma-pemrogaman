# Pardede Putra Anjasmara
# 2505060061

# Luas Persegi Panjang
def luas_pp():
  panjang = int(input('Masukkan panjang : '))
  lebar = int(input('Masukkan lebar : '))
  luasPP = panjang * lebar
  print(f'Luas persegi panjang : {luasPP}\n')
  return luasPP
luas_pp()

# Volume persegi panjang
def volume_pp():
  panjang = int(input('Masukkan panjang : '))
  lebar = int(input('Masukkan lebar : '))
  tinggi = int(input('Masukkan tinggi : '))
  volume = panjang * lebar * tinggi
  print(f'Volume persegi panjang : {volume}\n')
  return volume
volume_pp()

# Luas lingkaran
def luas_o():
  jari = int(input('Masukkan jari - jari : '))
  luas = jari * 2 * 3.14
  print(f'Luas lingkaran : {luas}\n')
  return luas
luas_o()

# Volume bola
def volume_bola():
  jari = int(input('Masukkan jari - jari : '))
  volume = jari * jari * 3.14
  print(f'Volume lingkaran : {volume}\n')
  return volume
volume_bola()