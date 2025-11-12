# Pardede Putra Anjasmara
# 2505060061
# Rombel Praktikum 4

import datetime
import os
import string
import random

# template data buku
buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun': 0,
    'tgl_pinjam': datetime.datetime(1111,1,11),
    'status': 'Tersedia'
}

data_buku = {}

while True:
    os.system("clear")  # gunakan "cls" kalau Windows

    print(f"{'SISTEM PERPUSTAKAAN':^40}")
    print("-"*40)

    # buat dictionary buku baru berdasarkan template
    buku = dict.fromkeys(buku_template.keys())
    buku['judul'] = input("Judul Buku       : ")
    buku['penulis'] = input("Penulis Buku     : ")
    buku['tahun'] = int(input("Tahun Terbit     : "))

    # input tanggal terakhir dipinjam
    TH = int(input("Tahun terakhir dipinjam (YYYY): "))
    BL = int(input("Bulan (1-12): "))
    TG = int(input("Tanggal (1-31): "))
    buku['tgl_pinjam'] = datetime.datetime(TH, BL, TG)

    # input status
    buku['status'] = input("Status Buku (Tersedia/Tidak): ")

    # buat key acak 6 huruf kapital
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_buku.update({KEY: buku})

    print("\nDATA BUKU TERSIMPAN\n")
    print(f"{'KEY':<8} {'Judul':<20} {'Penulis':<15} {'Tahun':<6} {'Tgl Pinjam':<12} {'Status'}")
    print("-"*80)

    for key in data_buku:
        JUDUL = data_buku[key]['judul']
        PENULIS = data_buku[key]['penulis']
        TAHUN = data_buku[key]['tahun']
        PINJAM = data_buku[key]['tgl_pinjam'].strftime("%x")
        STATUS = data_buku[key]['status']

        print(f"{key:<8} {JUDUL:<20} {PENULIS:<15} {TAHUN:<6} {PINJAM:<12} {STATUS}")

    print("\n")
    lanjut = input("Tambah buku lagi? (y/n): ")

    if lanjut == "n":
        break

print("\nProgram selesai, terima kasih!")
