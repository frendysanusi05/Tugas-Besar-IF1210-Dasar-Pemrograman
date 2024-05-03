import os, data
from fungsi_sakti import *
from account import *
from help import *
from misc import *
from modifygame import *
from showgame import *
from system import *

# KAMUS
# cek_login : bool
# username, password, id_user : string

# ALGORITMA PROGRAM UTAMA
cek_login = False
username = ""
password = ""
id_user = ""

def menu_awal():
# Menu Awal
# I.S : Menampilkan selamat datang dan memanggil fungsi login 
# F.S : Menampilkan menu baru jika berhasil login

  # KAMUS LOKAL
  # username, passsword, id_user : str
  # cek_login : bool

  # ALGORITMA
  global cek_login, username, password, id_user

  print("""
▒█▀▀▀█ █▀▀ █░░ █▀▀█ █▀▄▀█ █▀▀█ ▀▀█▀▀ 　 ▒█▀▀▄ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀▄ █▀▀▀ 　 █▀▀▄ ░▀░ 　 ▒█▀▀█ ░▀░ █▀▀▄ █▀▀█ █▀▄▀█ █▀▀█ 
░▀▀▀▄▄ █▀▀ █░░ █▄▄█ █░▀░█ █▄▄█ ░░█░░ 　 ▒█░▒█ █▄▄█ ░░█░░ █▄▄█ █░░█ █░▀█ 　 █░░█ ▀█▀ 　 ▒█▀▀▄ ▀█▀ █░░█ █░░█ █░▀░█ █░░█ 
▒█▄▄▄█ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░░▀ ▀░░▀ ░░▀░░ 　 ▒█▄▄▀ ▀░░▀ ░░▀░░ ▀░░▀ ▀░░▀ ▀▀▀▀ 　 ▀▀▀░ ▀▀▀ 　 ▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀▀▀▀\n""")
  
  cek_login, username, password, id_user = login()

  if (cek_login):
    Clear()
    menu()
  else:
    if (username == "" and password == ""):
      sys.exit()
    else:
      menu_awal()
# END OF menu_awal

def menu():
# Menu
# I.S : Pilihan sembarang dan menampilkan menu pilihan ke layar
# F.S : Memanggil fungsi sesuai masukan 
  
  # KAMUS LOKAL
  # cek_login, admin : bool
  # pilihan, username, password, id_user : string
  # hanya_admin, hanya_user : string
  
  # ALGORITMA
  global cek_login, username, password, id_user
  
  print("""\nDaftar menu:
-------------------------
F02 - register
F03 - login
F04 - tambah_game
F05 - ubah_game
F06 - ubah_stok
F07 - list_game_toko
F08 - buy_game
F09 - list_game
F10 - search_my_game
F11 - search_game_at_store
F12 - topup
F13 - riwayat
F14 - Help
F16 - save
F17 - exit
B02 - Magic Conch Shell
B03 - Game Tic-Tac-Toe
T01 - change_admin_or_user
  """)
  admin = cek_role(username)
  hanya_admin = "Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut."
  hanya_user = "Maaf, anda harus menjadi user untuk melakukan hal tersebut."
  pilihan = input("Masukkan pilihan menu (F02 - F17/B02 - B03/T01): ").upper()
  Clear()
  
  if (pilihan == "F02"):
    if admin:
      register()
    else:
      print(hanya_admin)
      
  elif (pilihan == "F03"):
    cek_login, username, password, id_user = login()
    
  elif (pilihan == "F04"):
    if admin:
      tambah_game()
    else:
      print(hanya_admin)
      
  elif (pilihan == "F05"):
    if admin:
      ubah_game()
    else:
      print(hanya_admin)
      
  elif (pilihan == "F06"):
    if admin:
      ubah_stok()
    else:
      print(hanya_admin)
      
  elif (pilihan == "F07"):
    list_game_toko()
  
  elif (pilihan == "F08"):
    if admin:
      print(hanya_user)
    else:
      buy_game(id_user)
      
  elif (pilihan == "F09"):
    if admin:
      print(hanya_user)
    else:
      list_game(id_user)
     
  elif (pilihan == "F10"):
    if admin:
      print(hanya_user)
    else:
      search_my_game(id_user)
      
  elif (pilihan == "F11"):
    search_game_at_store()
    
  elif (pilihan == "F12"):
    if admin:
      topup()
    else:
      print(hanya_admin)
      
  elif (pilihan == "F13"):
    if admin:
      print(hanya_user)
    else:
      riwayat(id_user)
      
  elif (pilihan == "F14"):
    Help(admin)
  elif (pilihan == "F16"):
    save()
  elif (pilihan == "F17"):
    Exit()
  elif (pilihan == "B02"):
    kerangajaib()
  elif (pilihan == "B03"):
    tictactoe()
  elif (pilihan == "T01"):
    if admin:
      change_admin_or_user()
    else:
      print(hanya_admin)

  else:
    print("Tidak ada pilihan tersebut. Silakan pilih yang ada di menu.")
  Wait()
  menu()
# END OF menu

def cek_role(username):
# Fungsi cek_role
# Mengembalikan nilai True jika role pengguna adalah admin

  # KAMUS LOKAL
  # valid : bool
  # i : int

  # ALGORITMA
  valid = False
  for i in range(Length(data.user)):
    if (username == data.user[i][1]) and (data.user[i][4] == "admin"):
      valid = True
  return valid
# END OF cek_role