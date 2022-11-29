# praktikum6

Program Data Mahasiswa Pada praktikum 5, kita akan membuat program sederhana untuk membuat data mahasiswa menggunakan Dictionary dengan python.

Codingan Praktikum 5 python x = {}

while True: c = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

if c.lower() == 't': print("Tambah Data") nama = input("Nama : ") nim = int(input("NIM : ")) uts = int(input("Nilai UTS : ")) uas = int(input("Nilai UAS : ")) tugas = int(input("Nilai Tugas : ")) akhir = tugas30/100 + uts35/100 + uas*35/100 x[nama] = nim, uts, uas, tugas, akhir

elif c.lower() == 'u': print("Ubah Data") nama = input("Masukkan Nama : ") if nama in x.keys(): nim = int(input("NIM : ")) uts = int(input("Nilai UTS : ")) uas = int(input("Nilai UAS : ")) tugas = int(input("Nilai Tugas : ")) akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100 x[nama] = nim, uts, uas, tugas, akhir else: print("Nama {0} tidak ditemukan".format(nama))

elif c.lower() == 'h': print("Hapus Data") nama = input("Masukkan Nama : ") if nama in x.keys(): del x[nama] else: print("Nama {0} Tidak Ditemukan".format(nama))

elif c.lower() == 'c': print("Cari Data") nama = input("Masukkan Nama : ") if nama in x.keys(): print("="*73) print("| Daftar Mahasiswa |") print("="*73) print("| Nama | NIM | UTS | UAS | Tugas | Akhir |") print("="*73) print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |" .format(nama, nim, uts, uas, tugas, akhir)) print("="*73) else: print("Nama {0} Tidak Ditemukan".format(nama))

elif c.lower() == 'l': if x.items(): print("="*78) print("| Daftar Mahasiswa |") print("="*78) print("|No. | Nama | NIM | UTS | UAS | Tugas | Akhir |") print("="*78) i = 0 for z in x.items(): i += 1 print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |" .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i)) print("=" * 78) else: print("="*78) print("| Daftar Mahasiswa |") print("="*78) print("|No. | Nama | NIM | UTS | UAS | Tugas | Akhir |") print("="*78) print("| TIDAK ADA DATA |") print("="*78)

elif c. lower() == 'k': break

else: print("Pilih menu yang tersedia") Penjelasan : 1.) Pertama kita membuat sebuah dictionary kosong yang nantinya akan diinputkan data ketika program dijalankan. python

Gambar 1
<img width="358" alt="Jepretan Layar 2022-11-28 pukul 15 22 52" src="https://user-images.githubusercontent.com/116137842/204453481-8dff9c34-d71a-4bd7-b5ac-c711388bd8e3.png">



2.) Lalu kita membuat kondisi perulangan dan sebuah keterangan untuk pilihan menu yang akan menjalankan program. python Gambar 2
<img width="905" alt="Jepretan Layar 2022-11-28 pukul 15 25 30" src="https://user-images.githubusercontent.com/116137842/204453519-b173a6ea-5763-4bb4-b427-1f447bf7e1b3.png">

3.) Membuat syntax untuk menambahkan data. python Gambar 3

Disini a<img width="612" alt="Jepretan Layar 2022-11-29 pukul 13 19 07" src="https://user-images.githubusercontent.com/116137842/204453923-ec139e76-33a7-4f13-b226-0e45547d84e8.png">
pabila kita menginputkan 't' maka kita akan diminta untuk menginputkan beberapa data. Data yang kita inputkan akan masuk ke dictionary 'x' yang telah dibuat tadi dengan data 'nama' sebagai keys dan sisanya sebagai valuesnya.

4.) Membuat syntax untuk mengubah data. python Gambar 4
<img width="650" alt="Jepretan Layar 2022-11-29 pukul 13 21 15" src="https://user-images.githubusercontent.com/116137842/204454331-f37d44c8-08ba-4d1f-ba18-fea23aab09db.png">

Apabila kita menginput 'u' maka akan ada keterangan untuk mengubah data dan kita akan diminta untuk menginputkan nama yang mau diubah datanya, apabila nama tidak ada maka outputnya "Nama {} tidak ditemukan". Dimana {} adalah nama/data yang mau kita ubah.

5.) Membuat syntax untuk menghapus data. python Gambar 5
<img width="571" alt="Jepretan Layar 2022-11-29 pukul 13 23 16" src="https://user-images.githubusercontent.com/116137842/204454503-7d6d2ad0-5ef1-433f-b114-6a5a012b9c63.png">

Apabila kita menginput 'h' maka kita akan diminta menginput nama yang akan dihapus. Jika nama ada di dalam dictionary, maka system akan menghapus keys/nama tersebut beserta valuesnya pada statement del x[nama].

6.) Membuat syntax untuk mencari data. python Gambar 6

Apab<img width="634" alt="Jepretan Layar 2022-11-29 pukul 13 24 29" src="https://user-images.githubusercontent.com/116137842/204454680-944a80b3-4fc7-4d2e-858a-cc6c37047677.png">
ila kita menginputkan 'c' maka kita akan diminta untuk memasukkan nama yang akan dicari. Apabila nama yang dicari ada di dalam dictionary maka outputnya akan menampilkan data dari nama tersebut.

7.) Membuat syntax untuk melihat atau menampilkan data. python Gambar 7
<img width="604" alt="Jepretan Layar 2022-11-29 pukul 13 25 23" src="https://user-images.githubusercontent.com/116137842/204454824-2e486a52-fb7e-414c-9eac-6901a69dc4aa.png">

Apabila kita menginput 'l' maka sistem akan menampilkan data - data yang sudah kita masukkan. Jika kita belum memasukkan data maka outputnya menjadi "TIDAK ADA DATA".

8.) Membuat syntax untuk menghentikan perulangan. python
<img width="451" alt="Jepretan Layar 2022-11-29 pukul 13 26 21" src="https://user-images.githubusercontent.com/116137842/204455025-c2f15443-613c-4f07-b340-00defde4e6aa.png">

Gambar 8

Apabila kita menginput 'k' maka program akan langsung berhenti.

9.) Membuat syntax untuk apabila memilih pilihan yang tidak ada di menu. python Gambar 9 Jika kita menginputkan selain yang ada pada menu (t, u, h, c, l, k) maka kita akan diminta untuk memilih menu yang tersedia.
<img width="468" alt="Jepretan Layar 2022-11-29 pukul 13 27 32" src="https://user-images.githubusercontent.com/116137842/204455189-a4378fa0-d27a-41ff-a228-d574e2661183.png">

# COCDE PROGRAM

<img width="1280" alt="latihan 1" src="https://user-images.githubusercontent.com/116137842/204456822-8a2884ce-6b53-4ac4-807c-df38080aeb6d.png">

<img width="1280" alt="latihan 2" src="https://user-images.githubusercontent.com/116137842/204456963-506b04e0-958a-4ab6-a45a-983e6a9120e8.png">

<img width="1280" alt="praktikum 3" src="https://user-images.githubusercontent.com/116137842/204457028-e7a0e292-dcde-4777-afd1-ddfa78717f0c.png">

