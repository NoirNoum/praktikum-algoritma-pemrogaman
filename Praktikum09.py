# Pardede Putra Anjasmara
# 2505060061
# Rombel Praktikum 04

# NOMER 1
buah = ['apel', 'mangga', 'jeruk', 'anggur', 'pisang']
print(buah)

# a.) tambahkan "semangka" di akhir list
buah.append('semangka')
print(f"\nsetelah ditambah diakhir : {buah}")

# sisipkan 'durian' di antara 'jeruk' dan 'anggur'
buah.insert(3, 'durian')
print(f"\nsetelah ditambah di antara 'jeruk' dan 'anggur': {buah}")

# hapus 'mangga' dari list
buah.remove('mangga')
print(f'\nsetelah dihapus : {buah}')

# ubah 'pisang' menjadi 'nanas'
buah[4] = 'nanas'
print(f'\nsetelah diubah : {buah}')

# tampilkan 3 buah pertama
tiga_buah_pertama = buah[:3]
print(f'\ntiga buah pertama adalah : {tiga_buah_pertama}')
print('===================================================================')

# NOMER 2
angka = [45, 12, 78, 23, 56, 89, 34]
print(angka)

# urutkan list secara ascending
angka.sort()
print(f'\nlist setelah diurutkan secara ascending : {angka}')

# urutkan list secara descending
angka.reverse()
print(f'\nlist setelah diurutkan secara descending : {angka}')
