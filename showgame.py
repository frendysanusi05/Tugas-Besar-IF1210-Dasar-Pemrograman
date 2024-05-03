import data
from fungsi_sakti import *

def list_game_toko():
# F07 - Listing Game di Toko Berdasarkan ID, Tahun Rilis dan Harga
# Akses: User dan Admin
# I.S : pilih_skema terdefinisi  
# F.S : menampilkan list game pada toko berdasarkan tahun+, tahun-, 
#   	harga+, harga-,atau kosong (tekan tombol Enter)} 

  # KAMUS LOKAL
  # pilih_skema : str
  # Temp : array of Game

  # ALGORITMA
  print("""
Skema sorting:
- tahun+ = sorting daftar game secara menaik berdasarkan tahun
- tahun- = sorting daftar game secara menurun berdasarkan tahun
- harga+ = sorting daftar game secara menaik berdasarkan harga
- harga- = sorting daftar game secara menurun berdasarkan harga

Jika tidak ingin men-sorting daftar game, silakan tekan Enter.    
  """)

  print("Masukkan input berupa tahun+, tahun-, harga+, harga-, atau kosong (tekan tombol Enter).")
  pilih_skema = input("Skema sorting: ").lower()
  Temp = []
  Wait()
  if (pilih_skema == "tahun+"):
    Ascending(3)
  elif (pilih_skema == "harga+"):
    Ascending(4)
  
  elif (pilih_skema == "tahun-"):
    Descending(3)
  elif (pilih_skema == "harga-"):
    Descending(4) 

  elif (pilih_skema == ""):
    Ascending(0)

  else:
    print("Skema sorting tidak valid!")
# END F07


def Ascending(indeks):
# Keperluan F07
# I.S : indeks terdefinisi 
# F.S : mencetak list game di toko dengan terurut membesar
  
  # KAMUS LOKAL
  # i, j, IMin : int
  # Temp : array of Game
    
  # ALGORITMA
  print("0. Id | Nama | Harga | Kategori | Tahun_rilis | Stok")
  for i in range(1, Length(data.game)):
    IMin = i
    for j in range(i+1, Length(data.game)):
      if (str(data.game[j][indeks]) < str(data.game[IMin][indeks])):
        IMin = j
    Temp = data.game[i]
    data.game[i] = data.game[IMin]
    data.game[IMin] = Temp       
  CetakSorting()
# END OF Ascending


def Descending(indeks):
# Keperluan F07
# { I.S : indeks terdefinisi 
# F.S : mencetak list game di toko dengan terurut mengecil 
  
  # KAMUS
  # i, j, IMax : int
  # Temp : array of Game
  
  # ALGORITMA 
  print("0. Id | Nama | Harga | Kategori | Tahun_rilis | Stok")
  for i in range(1, Length(data.game)):
    IMax = i
    for j in range(i+1, Length(data.game)):
      if (str(data.game[j][indeks]) > str(data.game[IMax][indeks])):
        IMax = j
    Temp = data.game[i]
    data.game[i] = data.game[IMax]
    data.game[IMax] = Temp       
  CetakSorting()
# END OF Descending


def CetakSorting():
# I.S : data.game berisi data csv 
# F.S : mencetak data.game ke layar secara terurut
  
  # KAMUS
  # count, i, j : int

  #  ALGORITMA
  count = 0
  for i in range(1, Length(data.game)):
    count += 1
    print(f"{count}.", end = " ")
  
    for j in range(6):
      if (j != 5):
        if (j == 0) or (j == 1):
          print(data.game[i][j], end=" | ")
        elif (j == 2):
          print(data.game[i][4], end=" | ")
        else:
          print(data.game[i][j-1], end=" | ")  
      else:
        print(data.game[i][j])
# END OF CetakSorting


def list_game(user_id):
# Fungsi F09 - Melihat Game yang Dimiliki
# Akses : User only
# I.S : user_id sembarang 
# F.S : Mencetak semua game yang dimiliki oleh user dengan user_id tersebut ke layar

  # KAMUS LOKAL
  # game_yang_dimiliki : array of string
  # i : int

  # ALGORITMA
  game_yang_dimiliki = []

  for i in data.kepemilikan:
    if(user_id == i[1]):
      game_yang_dimiliki = Append(game_yang_dimiliki, i[0])

  if Length(game_yang_dimiliki) == 0:
	  print("Anda belum memiliki game! Silahkan beli dengan command F08!")
  else:
    count = 1
    Wait()

    print("Daftar Game:")
    print("0. Id | Nama | Kategori | Tahun_rilis | Harga | Stok")
    for i in game_yang_dimiliki:   
      game_index = getIndexFromAttribute(i, 0, data.game)
      
      print("{}. {} | {} | {} | {}".format(count ,i, data.game[game_index][1], data.game[game_index][2], data.game[game_index][3], data.game[game_index][4]))
      count += 1
# END OF F09

def search_my_game(id_user):
# F10 - Mencari Game yang dimiliki dari ID dan tahun rilis
# Akses: User only
# I.S. id_user terdefinisi, ID dan tahun_rilis sembarang 
# F.S. Menampilkan hasil pencarian game milik useer ke layar berdasarkan ID dan tahun rilis

  # KAMUS LOKAL
  # ID, tahun_rilis : str
  # count, i, j, k : int
  # my_game : array of string
  
  # ALGORITMA
  ID = input("Masukkan ID Game: ")
  tahun_rilis = input("Masukkan Tahun Rilis Game: ")
  print("\nDaftar game pada inventory yang memenuhi kriteria:")

  Wait()
  count = 1
  my_game = []
  for i in range(Length(data.kepemilikan)):
    if (str(id_user) == str(data.kepemilikan[i][1])) and (ID == str(data.kepemilikan[i][0]) or ID == ""):
      my_game = Append(my_game, str(data.kepemilikan[i][0]))
     
  for j in range(Length(my_game)):
    for k in range(Length(data.game)):
      if (my_game[j] == data.game[k][0]) and (tahun_rilis == data.game[k][3] or tahun_rilis == ""):
        if (count == 1):
          print("0. Id | Nama | Kategori | Tahun_rilis | Harga | Stok")
        CetakGame(k, count)
        count += 1

  if (count == 1):
    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
# END OF F10

def search_game_at_store():
# F11 - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis 
# Akses: Admin dan User
# I.S. ID, nama, harga, kategori, dan tahun_rilis sembarang 
# F.S. Menampilkan hasil pencarian game ke layar berdasarkan ID, nama, harga, kategori, dan tahun_rilis

  # KAMUS LOKAL
  # ID, nama, harga, kategori, tahun_rilis : str
  # count, i : int
  
  # ALGORITMA
  ID = input("Masukkan ID Game: ")
  nama = input("Masukkan Nama Game: ")
  harga = input("Masukkan Harga Game: ")
  kategori = input("Masukkan Kategori Game: ")
  tahun_rilis = input("Masukkan Tahun Rilis Game: ")
  print('\nDaftar game pada toko yang memenuhi kriteria:')

  Wait()
  count = 1
  for i in range(1, Length(data.game)):
    # masukan masing-masing masukan parameter boleh kosong
    if (ID == data.game[i][0] or ID == '') and (nama == data.game[i][1] or nama == '') and (kategori == data.game[i][2] or kategori == '') and (tahun_rilis == data.game[i][3] or tahun_rilis == '') and (harga == data.game[i][4] or harga == ''):
      if (count == 1):
        print("0. Id | Nama | Kategori | Tahun_rilis | Harga | Stok")
      CetakGame(i, count)
      count += 1
            
  if (count == 1):
    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
# END F11


def CetakGame(indeks, count):
# Prosedur CetakGame
# Keperluan: F10, F11
# Mencetak hasil pencarian ke layar

  # KAMUS LOKAL
  # j : int
  
  # ALGORITMA
  print(f"{count}.", end = " ")
  for j in range(6):
    if (j != 5):
      print(data.game[indeks][j], end=" | ")
    else:
      print(data.game[indeks][j])
# END OF CetakGame


def riwayat(user_id):
# F13 - Melihat Riwayat Pembelian
# Akses : User Only
# Melihat riwayat pembelian game 
  
  # KAMUS LOKAL
  # riwayat_index, I : int
  # riwayat_user : array of Riwayat

  # ALGORITMA
  riwayat_user = []
  for i in data.riwayat :
    if (str(user_id) == str(i[3])) :
      riwayat_user = Append(riwayat_user, i)
  if riwayat_user == [] : # user tidak memiliki riwayat
    print("Maaf, kamu tidak memiliki riwayat pembelian game. Ketik perintah F08 untuk membeli.")
  else :
    print("0. ID | Nama Game | Harga | Tahun_Beli")
    for i in range (Length(riwayat_user)) :
      if (str(user_id) == str(riwayat_user[i][3])):
        print(f"{i+1}. {riwayat_user[i][0]} | {riwayat_user[i][1]} | {riwayat_user[i][2]} | {riwayat_user[i][4]}") 
# END OF F13