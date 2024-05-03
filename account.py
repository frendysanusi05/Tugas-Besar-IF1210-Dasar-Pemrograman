import data
from misc import *
from fungsi_sakti import *

def register():
# F02 - Register
# Akses: Admin onl\y
# I.S. nama, username, dan password sembarang
# F.S. Mencetak pesan ke layar apakah berhasil register atau tidak

  # KAMUS LOKAL
  # nama, username, password : str
  # count, i : int
  # ada : bool
  
  # ALGORITMA
  nama = input("Masukan nama: ")
  username = input("Masukan username: ")
  
  while not validasi_user(username):
    Wait()
    print("Username tidak valid. Silakan masukan username lagi!")
    username = input("Masukan username: ")
    
  password = input("Masukan password: ")
  password = encrypt(password, 5, 9)

  count = 0
  ada = False
  for i in range(Length(data.user)):
    count += 1
    if (username == data.user[i][1]):
      ada = True

  Wait()
  if ada:
    print(f"Username {nama} sudah terpakai, silakan menggunakan username lain.")
  else:
    if (nama == "") or (username == "") or (password == ""):
      print("Ada masukan yang kosong. Register gagal!")
    else:
      print(f"Username {nama} telah berhasil register ke dalam 'Binomo'")
      data.user = Append(data.user, [count, username, nama, password, "user", 0])
# END OF F02

def validasi_user(username):
# Fungsi validasi_user
# Keperluan: F02
# Mengembalikan True jika masukan username benar

  # KAMUS LOKAL
  # i: int
  # valid: bool
  
  # ALGORITMA
  i = 0
  valid = True
  while (i < Length(username)) and valid:
    if (ord(username[i].lower()) < 97 or ord(username[i].lower()) > 122) and (username[i] != '-') and (username[i] != '_') and (ord(username[i]) < 48 or ord(username[i]) > 57):
      valid = False
    i += 1
  return valid
# END OF validasi_user

def login():
# F03: Login
# AKses: User dan Admin
# Akses masuk ke program jika masukan username dan password benar

  # KAMUS LOKAL
  # login : bool
  # username, password : str
  # indeks, i, id_user : int
    
  # ALGORITMA
  login = False
  print("Login: ")
  username = input("Masukan username: ")
  password = input("Masukan password: ")
  password = encrypt(password, 5, 9)
    
  indeks = -9999
  for i in range(Length(data.user)):
    if (username == data.user[i][1]) and (password == data.user[i][3]):
      indeks = i

  Wait()
  if (indeks != -9999):
    print(f"Halo {data.user[indeks][2]}! Selamat datang di 'Binomo'.")
    login = True
  else:
    print("Password atau username salah atau tidak ditemukan.")
  
  id_user = getIndexFromAttribute(username, 1, data.user)
  id_user = data.user[id_user][0]

  return login, username, password, id_user
# END OF F03

def topup () :
# F12 - Topup
# Akses : Admin Only
# I.S : username dan saldo sembarang
# F.S : mencetak username dan nilai saldo akhir yang tervalidasi 

  
  # KAMUS LOKAL
  # username : string
  # user_index, saldo_akhir, saldo, saldo_awal : int

  # ALGORITMA
	username = input("Masukan username: ")
	user_index = getIndexFromAttribute (username, 1, data.user)

	try:
		saldo = int(input("Masukkan saldo: "))
		Wait()
	# Username terdaftar
		if user_index != 0 :
			saldo_awal = int(data.user[user_index][5])
			saldo_akhir = saldo + saldo_awal
			if saldo_akhir < 0 :
				print("Masukan tidak valid! Nilai yang dikurangin melebihi saldo user.")
			else:
				if saldo_akhir > saldo_awal:
					print("Top-up berhasil! Saldo", username, "bertambah menjadi", str(saldo_akhir))
				else:
					print("Top-up berhasil! Saldo", username, "berkurang menjadi", str(saldo_akhir))
				data.user[user_index][5] = saldo_akhir
			# Username tidak terdaftar
		else :
			print("Username", '"' + username + '"', "tidak ditemukan")
	except ValueError:
		print("Masukan tidak valid! Saldo harus berupa bilangan bulat.")
# END OF F12