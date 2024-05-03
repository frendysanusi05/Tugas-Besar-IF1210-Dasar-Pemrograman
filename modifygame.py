import data
from fungsi_sakti import *
import sys, os, argparse

def tambah_game ():
# F04 - Menambah Game ke Toko Game
# Akses : Admin Only
# I.S : nama, kategori, tahun_rilis, harga, stok sembarang 
# F.S : Seluruh data atribut game terdefinisi
  
  # KAMUS LOKAL
  # validate = boolean
  # banyak_data, id_game = string

  # ALGORITMA
  validate = False
  banyak_data = str(Length(data.game))
  if Length(banyak_data) == 1:
    id_game = "G00" + banyak_data
  elif Length(banyak_data) == 2:
    id_game = "G0" + banyak_data
  else:
    id_game = "G" + banyak_data
  
  while not validate:
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok = input("Masukkan stok awal: ")

    Wait()
    if Length(nama) == 0 or Length(kategori) == 0 or Length(tahun_rilis) == 0 or Length(harga) == 0 or Length(stok) == 0 :
      Clear()
      print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
    else :
      data.game = Append(data.game,[id_game,nama,kategori,int(tahun_rilis), int(harga), int(stok)])
      print("Selamat! Berhasil menambahkan game", nama)
      validate = True
# END OF F04

def ubah_game () :
# F05 - Mengubah Game pada Toko Game
# Akses : Admin Only
# I.S : game_id, nama, kategori, tahun_rilis, harga sembarang 
# F.S : Menampilkan game_id, nama, kategori, tahun_rilis, dan harga yang 
#		telah diubah jika masukkan tidak kosong
  
  # KAMUS LOKAL
  # game_id = str
  # id_index, i = int

  # ALGORITMA
  game_id = input("Masukkan ID game: ")
  id_index = getIndexFromAttribute (game_id, 0, data.game)

  if id_index == 0 :
    print("Tidak ada game dengan ID tersebut!")
  else :
    print()
    print("Data sebelum diubah adalah: ")
    print("[Nama Game, Kategori, Tahun Rilis, Harga, Stok]")
    for i in range (6) :
      if i == 0 :
        print("[", end="")
      elif i == 5 :
        print(str(data.game[id_index][i])+"]")
      else :
        print(str(data.game[id_index][i]),end=", ")
        
    print()
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    print()
  
    # print data sekarang
    if Length(nama) != 0 :
      data.game[id_index][1] = nama
    if Length(kategori) != 0 :
      data.game[id_index][2] = kategori
    if Length(tahun_rilis) != 0 :
      data.game[id_index][3] = int(tahun_rilis)
    if Length(harga) != 0 :
      data.game[id_index][4] = int(harga)

    Wait()
    print()
    print("Data yang sudah diubah adalah: ")
    print("[Nama Game, Kategori, Tahun Rilis, Harga, Stok]")
    for i in range (6) :
      if i == 0 :
        print("[", end="")
      elif i == 5 :
        print(str(data.game[id_index][i])+"]")
      else :
        print(str(data.game[id_index][i]),end=", ")
# END OF F05

def ubah_stok():
# F06 - Ubah Stok
# I.S : game_id dan jumlah_tambahan sembarang
# F.S : mengupdate stok game dengan game_id input sebanyak 
#       tambahan sesuai input jumlah_tambahan kemudian dicetak 
#       perubahan / tidak perubahannya 

	# KAMUS LOKAL
	# game_id, game_nama : string
	# game_index, jumlah_tambahan, game_stok, game_stok_baru : int
	
	# ALGORITMA
	# input dari user
	game_id = input("Masukkan ID game: ")
	game_index = getIndexFromAttribute(game_id, 0, data.game)

	if(game_index != 0):
		jumlah_tambahan = None
		while jumlah_tambahan == None:
			try:
				jumlah_tambahan = int(input("Masukkan jumlah: "))
			except ValueError:
				print("Mohon masukkan bilangan bulat!")
			
		game_nama = data.game[game_index][1]
		game_stok = int(data.game[game_index][5])

		game_stok_baru = game_stok + jumlah_tambahan
		Wait()
		if(game_stok_baru >= 0):
			data.game[game_index][5] = str(game_stok_baru)
			if(game_stok_baru > game_stok):
				print("Stok game {} berhasil ditambahkan. Stok sekarang: {}".format(game_nama, game_stok_baru))
			else:
				print("Stok game {} berhasil dikurangi. Stok sekarang: {}".format(game_nama, game_stok_baru))
		else:
			print("Stok game {} gagal dikurangi karena stok kurang. Stok sekarang: {} (< {})".format(game_nama, game_stok, abs(jumlah_tambahan)))
	else:
		print("Tidak ada game dengan ID tersebut!")
# END OF F06

def buy_game(user_id):
# F08 - Beli Game
# I.S : game_id dan user_id sembarang
# F.S : menambahkan game dengan game_id sesuai input ke dalam 
#       kepemilikan user dengan user_id sesuai input, mengurangi 
#       saldo user, dan mengurangi stok game bila berhasil 
#       terbeli

	# KAMUS LOKAL
	# game_id, game_nama, user_id : string
	# game_index, user_index, game_harga, game_stok, user_saldo : int
	# punyaGame : bool
	
	# ALGORITMA
	game_id = input("Masukkan ID game: ")
	game_index = getIndexFromAttribute(game_id, 0, data.game)
	user_index = getIndexFromAttribute(user_id, 0, data.user)

	if(game_index != 0):
		# inisialisasi variable untuk perubahan lokal
		game_nama = data.game[game_index][1]
		game_harga = int(data.game[game_index][4])
		game_stok = int(data.game[game_index][5])
		user_id = data.user[user_index][0]
		user_saldo = int(data.user[user_index][5])
		# kepemilikan = data.kepemilikan[game_index][1]

		punyaGame = False
		Wait()
		for milik in data.kepemilikan:
			if(milik[0] == game_id and milik[1] == user_id):
				punyaGame = True

		# Aturan checking : punyaGame? -> adaStok? -> saldoCukup?
		if not (punyaGame):
			if(game_stok > 0):
				if(user_saldo >= game_harga):
					# update perubahan lokal
					user_saldo -= game_harga
					game_stok -= 1

					# update perubahan lokal ke variable global
					data.user[user_index][5] = str(user_saldo)
					data.kepemilikan = Append(data.kepemilikan, [game_id, user_id])
					data.game[game_index][5] = str(game_stok)
					data.riwayat = Append(data.riwayat, [game_id, game_nama, str(game_harga), user_id, '2022'])

					print("Game “{}” berhasil dibeli!".format(game_nama))
				else:
					print("Saldo anda tidak cukup untuk membeli Game tersebut!")
			else:
				print("Stok Game tersebut sedang habis!")
		else:
			print("Anda sudah memiliki Game tersebut!")
	else:
		print("Game tidak ditemukan!")
# END OF F08