import time, data
from fungsi_sakti import *

def encrypt(plain, a, b):
# B01 (1) - Cipher
# Mengembalikan hasil enkripsi text plain menggunakan affine cipher dengan key a dan b

	# KAMUS LOKAL
	# crypted, plain : string
	# chara : character
	# a, b, i : integer

	# ALGORITMA
	crypted = ""
	for i in plain:
		chara = i
		if 48 <= ord(chara) <= 57 or ord(chara) == 32:  # character angka atau spasi
			crypted += chara
			continue
		elif 97 <= ord(chara) <= 122: # character bukan kapital
			crypted += chr((a*(ord(chara) - ord('a'))+b)%26 + ord('a'))
		elif 65 <= ord(chara) <= 90:  # character kapital
			crypted += chr((a*(ord(chara) - ord('A'))+b)%26 + ord('A'))
	return crypted
# END OF BO1 (1)
  
def decrypt(crypted, a, b):
# B01 (2) - Cipher
# Mengembalikan hasil dekripsi text yang terenkripsi menggunakan affine cipher dengan key a dan b

	# KAMUS LOKAL
	# crypted, plain : string
	# chara : character
	# a, b, i : integer

	# ALGORITMA
	plain = ""
	for i in crypted:
		chara = i
		if 48 <= ord(chara) <= 57 or ord(chara) == 32:  # character angka atau spasi
			plain += chara
			continue
		elif 97 <= ord(chara) <= 122: # character bukan kapital
			plain += chr(((inverse_modulo(a)*(ord(chara) - ord('a') - b))% 26) + ord('a'))
		elif 65 <= ord(chara) <= 90:  # character kapital
			plain += chr(((inverse_modulo(a)*(ord(chara) - ord('A') - b))% 26) + ord('A'))
	return plain
# END OF BO1 (2)
  
def egcd(a, b):
# B01 (3) - Cipher
# Merupakan fungsi fpb extended yang mengembalikan nilai fpb serta x dan y yang merupakan koefisien identitas Bézout yang memenuhi persamaan ax + by = fpb(a,b)

	# KAMUS LOKAL
	# a, b, fpb, y, x : integer

	# ALGORITMA
    if a == 0:
        return (b, 0, 1)
    else:
        fpb, y, x = egcd(b % a, a)
        return (fpb, x - (b // a) * y, y)
# END OF BO1 (3)

def inverse_modulo(a):
# B01 (4) - Cipher
# Mengembalikan hasil inverse modulo yang memenuhi persamaan x ≡ a^-1 (mod m) menggunakan identitas Bézout

	# KAMUS LOKAL
	# a, m, x, y, fpb : integer

	# ALGORITMA
    m = 26
    fpb, x, y = egcd(a, m)
    if fpb != 1:
        return None
    else:
        return x % m
# END OF BO1 (4)

def kerangajaib():
# B02 - Magic Conch Shell
# Akses : User dan Admin
# I.S : tanya sembarang 
# F.S : Mencetak jawaban ke layar secara acak

  # KAMUS LOKAL
  # tanya : string
  # jawaban : array of string
  # LCG, i : int
  
  # ALGORITMA
  tanya = input("Apa pertanyaannmu? ")
  jawaban = ["Ya", "Tidak", "Bisa Jadi", "Mungkin", "Tentunya", "Tidak mungkin"]
  LCG = round((time.time()*Length(tanya) + 2022) % (Length(jawaban)-1))
  # Menggunakan algoritma LCG yaitu (a*x + c) % m. Pada program ini, a = waktu saat ini (dalam satuan detik), x = jumlah karakter pada variabel tanya, c = konstanta tahun pembuatan program, yaitu 2022, dan m = jumlah kata pada array jawaban dikurang 1 (karena indeks dimulai dari 0)
  
  for i in range(Length(jawaban)):
    if (LCG == i):
      print("Menunggu jawaban dalam beberapa detik...")
      Wait()
      print(jawaban[i])
# END OF B02
      
def tictactoe():
# B03 (1) - Game Tic-Tac-Toe
# I.S : X, Y sembarang
# F.S : Mencetak kondisi akhir game ke layar }

  # KAMUS LOKAL
  # papan : array of array of char
  # i : int
  # X, Y : char
  # selesai : bool
  
  # ALGORITMA
  print("""
Legenda:
# Kosong
X Pemain 1
O Pemain 2
  """)

  papan = [['#' for i in range(3)] for j in range(3)]
  cetak_papan(papan)
  i = 0
  selesai = False
  while (i < 9) and not selesai:
    cek_pemain(i)
    X = input("X: ")
    Y = input("Y: ")

    while not validasi_input(papan, X, Y):
      Clear()
      cetak_papan(papan)
      print("Kotak tidak valid.")
      cek_pemain(i)
      X = input("X: ")
      Y = input("Y: ")

    if (i % 2): # Pemain 2 ('O')
      papan[int(X)][int(Y)] = 'O'
    else: # Pemain 1 ('X')
      papan[int(X)][int(Y)] = 'X'
    
    Clear()
    cetak_papan(papan)

    if(game_end(win_condition(papan))):
      Wait()
      selesai = True
    i += 1
# END OF B03 (1)
    
def cetak_papan(papan):
# B03 (2) - Game Tic-Tac-Toe
# Procedure cetak_papan
# I.S. papan terdefinisi
# F.S. Mencetak status papan ke layar

  # KAMUS LOKAL
  # row, col : int
  
  # ALGORITMA
  print("Status Papan")
  for row in range(3):
    for col in range(3):
      print(papan[row][col], end="")
    print()
# END OF BO3 (2)

def cek_pemain(i):
# B03 (3) - Game Tic-Tac-Toe
# Procedure cek_pemain
# I.S. i terdefinisi
# F.S. Mencetak ke layar apakah sekarang giliran pemain 1 atau 2

  # KAMUS LOKAL

  # ALGORITMA
  if (i % 2):
    print("Giliran Pemain 2 ('O') ")
  else:
    print("Giliran Pemain 1 ('X') ")
# END OF BO3 (3)

def validasi_input(papan, X, Y):
# B03 (4) - Game Tic-Tac-Toe
# Function validasi_input
# Mengembalikan nilai True jika X dan Y memenuhi syarat

  # KAMUS LOKAL

  # ALGORITMA
  try:
    X = int(X)
    Y = int(Y)
  except ValueError:
    return False
	
  if (X < 0 or X > 2) or (Y < 0 or Y > 2) or (papan[X][Y] == 'X') or (papan[X][Y] =='O'):
    return False
  # elif (0 <= int(X) <= 2) and (0 <= int(Y) <= 2):
    # if (papan[int(X)][int(Y)] == 'X') or (papan[int(X)][int(Y)] =='O'):
    #   return False
  else:
    return True
# END OF BO3 (4)

def win_condition(papan):
# B03 (5) - Game Tic-Tac-Toe
# Mengembalikan kode untuk menentukan hasil game; -1 bila game belum berakhir, 0 bila game seri, 1 bila X menang, 2 bila O menang

  # KAMUS LOKAL
  # papan : array of array of int
  # seri : bool
  # i : int
	
  # ALGORITMA
  # Check game seri
  seri = True
  for i in papan:
    for j in i:
      if(j == '#'):
        seri = False

        
  # Check game diagonal
  if(papan[0][0] == 'X' and papan[1][1] == 'X' and papan[2][2] == 'X') or (papan[0][2] == 'X' and papan[1][1] == 'X' and papan[2][0] == 'X'):
    return 1
  
    
  if(papan[0][0] == 'O' and papan[1][1] == 'O' and papan[2][2] == 'O') or (papan[0][2] == 'O' and papan[1][1] == 'O' and papan[2][0] == 'O'):
    return 2
  
  # Check game horizontal
  for i in papan:
    if(i[0] == 'X' and i[1] == 'X' and i[2] == 'X'):
      return 1
    elif(i[0] == 'O' and i[1] == 'O' and i[2] == 'O'):
      return 2

  # Check game vertikal
  for i in range(3):
    if(papan[0][i] == 'X' and papan[1][i] == 'X' and papan[2][i] == 'X'):
      return 1
    elif(papan[0][i] == 'O' and papan[1][i] == 'O' and papan[2][i] == 'O'):
      return 2

  if seri: return 0
  return -1
# END OF BO3 (5)

def game_end(x):
# B03 (6) - Game Tic-Tac-Toe
# Mencetak hasil game dan mengembalikan True apabila game sudah berakhir, False bila game belum berakhir 

  # KAMUS LOKAL
  # x : int
	
  # ALGORITMA
  if(x == 0):
    print("\nGame berakhir seri!")
  elif(x == 2):
    print("\nGame dimenangkan oleh player 'O'")
  elif(x == 1):
    print("\nGame dimenangkan oleh player 'X'")
  
  if(x >= 0): return True
  else: return False
# END OF BO3 (6)

def change_admin_or_user():
# T01 - Ganti Role User
# Mengubah role pada user.csv
# Masukan role hanya berupa admin atau user

  # KAMUS LOKAL
  # username, ubah_role : string
  # valid : bool
  # i : int
  
  # ALGORITMA
  username = input("Masukkan username yang ingin diganti rolenya: ")
  ubah_role = input("Role ingin diganti menjadi admin atau user?: ")
  Wait()
  valid = False
  for i in range(Length(data.user)):
    if (data.user[i][1] == username):
      data.user[i][4] = ubah_role
      print("Berhasil diubah!")
      valid = True

  if not valid:
    print("Username tidak ditemukan.")
# END OF change_admin_or_user