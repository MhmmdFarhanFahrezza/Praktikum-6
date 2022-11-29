# Latihan
print("Nama : m farhan f")
print("NIM  : 312210380")

daftarkontak = {"Nama": "Nomer Telepon"}
kontak = {'paul': '0812679888', 'bagus': '0856877776'}

# print
print("============================")
print("|   # Nama   |Nomor Telepon|")
print("============================")
print("|   # paul   |  ", kontak['paul'], '|')
print("|   # bagus   |  ", kontak['bagus'], '|')
print("============================")
print()

# Tampilkan kontaknya paul
print("# Tampilkan kontaknya paul")
print("===========================")
print("|    paul     | ", kontak['paul'], '|')
print("===========================")
print()

# Tambah kontak baru dengan nama iyan, nomor 087654544
print("# Tambah kontak baru dengan nama iyan, nomor 087654544")
kontak['iyan'] = '0877854544'
print("===========================")
print("|    iyan    | ", kontak['iyan'], '|')
print("===========================")
print()

# Ubah kontak bagus dengan nomor baru 088999776
print("# Ubah kontak bagus dengan nomor baru 088999776")
kontak['bagus'] = '0878987655'
print("===========================")
print("|    bagus    | ", kontak['bagus'], '|')
print("===========================")
print()

# Tampilkan semua Nama
print("# Tampilkan semua Nama")
print("==================================")
print(kontak.keys())
print("==================================")
print()

# Tampilkan semua Nomor
print("# Tampilkan semua Nomor")
print("====================================================")
print(kontak.values())
print("====================================================")
print()

# Tampilkan daftar Nama dan nomornya
print("# Tampilkan daftar Nama dan nomornya")
print("================================================================================")
print(kontak.items())
print("================================================================================")
print()

# Menghapus kontak bagus
print("# Hapus kontak bagus")
print("=========================================================")
kontak.pop('bagus')
print(kontak.items())
print("=========================================================")