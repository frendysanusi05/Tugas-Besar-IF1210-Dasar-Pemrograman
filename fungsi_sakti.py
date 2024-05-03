import os, time

def Length(kata):
# Mengembalikan jumlah karakter pada kata

  # KAMUS LOKAL
  # count, i : int

  # ALGORITMA
  count = 0
  for i in kata:
    count += 1
  return count
# END OF Length
  

def Append(ls, x):
# Menerima masukan sebuah array dan value, akan mengembalikan array baru yang memiliki value sebagai index terakhir

  # KAMUS LOKAL
  # lsLenght : integer
  # ls : array[1 ... lsLenght] of int/array/string/char
  # lsa : array[1 ... lsLenght+1] of int/array/string/char
    
  # ALGORITMA
  lsLenght = Length(ls)
    
  lsa = [0 for i in range(lsLenght+1)]
  for i in range(lsLenght):
    lsa[i] = ls[i]
  lsa[lsLenght] = x
  return lsa   
# END OF Append

    
def split(csv, pembatas):
# Menerima sebuah string dengan yang mana merupakan rangkaian kata dipisahkan oleh separator, fungsi akan mengembalikan masing-masing value kata tersebut dan disimpan kedalam list

  # KAMUS LOKAL
  # csv, kata : string
  # hasil[0 ... N] : array of string
  # pembatas : char
  # c : int
    
  # ALGORITMA
  hasil = []
  kata = ''
  for c in csv:
    if c != pembatas:
      kata += c
    else:
      hasil = Append(hasil, strip(kata))
      kata = ''
  hasil = Append(hasil, strip(kata))
  return hasil
# END OF split

def strip(kata, pembatas='\n'):
# Menerima sebuah string, fungsi akan mengembalikan string tanpa ada pembatas (seluruh instansi pembatas dihilangkan)

  # KAMUS LOKAL
  # hasil, kata : string
  # pembatas : char
  # i : int
	
  hasil = ""
  for i in kata:
    if i == pembatas:
      return hasil
    hasil += i
  return hasil
# END OF strip

def readCSV(fileloc):
# Menerima sebuah lokasi file csv yang akan dibaca dan mengembalikan array yang berisi seluruh value dalam csv dengan judul atribut di index 0
    
  # KAMUS LOKAL
  # fileloc, baris : string
  # kata : array of string
  # hasil : array of array
    
  # ALGORITMA
  with open(fileloc, 'r') as f:
    hasil = []
    for baris in f:
      kata = split(baris, ';')
      hasil = Append(hasil, kata)
    return(hasil)
# END OF readCSV

def getIndexFromAttribute(search, att, data):
# Fungsi untuk mendapatkan indeks dari pencarian sebuah value pada kolom array data yang akan dicari

  # KAMUS LOKAL
  # index, i, att : int
  # search : string
  # data : array of string

  # ALGORITMA
  index = 0
  for i in data:
    if i[att] == search:
      return index
    index += 1
  return 0
# END of getIndexFromAttribute

def Clear():
# Fungsi Clear
# Menghapus output sebelumnya

  # KAMUS LOKAL

  # ALGORITMA
  # os.system("clear") # untuk Linux
  os.system("cls") # untuk Windows
# END OF Clear

def Wait():
# Fungsi Wait
# Membuat jeda sebelum output ditampilkan

  # KAMUS LOKAL

  # ALGORITMA
  time.sleep(1)
# END OF Wait