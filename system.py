import data, os, sys, argparse
from fungsi_sakti import *

def load():
# F15 - Load
# Akses : User dan Admin pada command promt
# I.S : Nama folder penyimpanan sembarang 
# F.S : Membaca seluruh file csv pada folder dan menyimpannya  dalam array 

	# KAMUS LOKAL
	# dirpath, firnames, filenames, folders : array of string
	# dir_path, args.nama_folder : string
	
	# ALGORITMA
	parser = argparse.ArgumentParser()
	parser.add_argument('nama_folder', help="nama folder dimana file csv berada", nargs='?', const='')
	args = parser.parse_args()

	if args.nama_folder:
		dir_path = os.path.dirname(os.path.realpath(__file__))
		for (dirpath, dirnames, filenames) in os.walk(dir_path):
			folders = dirnames
			break

		if(args.nama_folder in folders):
			data.readAllCSV(args.nama_folder)
		else:
			print("Folder “{}” tidak ditemukan.".format(args.nama_folder))
			sys.exit()
	else:
		print("Tidak ada nama folder yang diberikan!\nUsage: python program_binomo.py <nama_folder>")
		sys.exit()
# END OF F15

def save():
# F15 - save
# I.S Lokasi sembarang, folder belum tentu ada pada lokasi tersebut
# F.S Folder terbuat sesuai lokasi dari input user dan di dalam folder 

	# KAMUS LOKAL
	# loc, path : string
	# folders : array of string
	
	# ALGORITMA
	loc = ""
	while loc == "":
		loc = input("Masukkan nama folder penyimpanan: ")
		if loc == "":
			print("Masukan tidak valid! Silahkan masukan nama folder penyimpanan.")

	dir_path = os.path.dirname(os.path.realpath(__file__))
	for (dirpath, dirnames, filenames) in os.walk(dir_path):
		folders = dirnames
		break
	
	path = os.path.join(dir_path, loc)
	if(loc in folders):
		pass
	else:
		os.makedirs(path)

	writeToCSV(path, data.user, "user")
	writeToCSV(path, data.game, "game")
	writeToCSV(path, data.kepemilikan, "kepemilikan")
	writeToCSV(path, data.riwayat, "riwayat")
# END OF F15	

def writeToCSV(path, data_array, data_name):
# Fungsi kebutuhan F15 - Save
# I.S : path, data_array, dan data_name sembarang 
# F.S : Terbentuk file <data_name>.csv yang berisikan data dalam array 
#	    data_array

	# KAMUS LOKAL
	# path, baris, data_name, baris_csv : string
	# data_array : array of string
	# f : SEQFILE of string

	# ALGORITMA
	path = os.path.join(path, (data_name + ".csv"))
	f = open(path, 'w')

	for baris in data_array:
		baris_csv = ""
		len = Length(baris)

		for i in range(len-1):
			baris_csv += str(baris[i]) + ';'
		baris_csv += str(baris[len-1]) + '\n'
		f.writelines(baris_csv)
# END OF writeToCSV

def Exit():
# F17 - Exit
# Akses : User dan Admin
# I.S : pilihan terdefinisi
# F.S : mengeksekusi pilihan dan keluar dari aplikasi 

  # KAMUS LOKAL
  # valid : bool
  # pilihan : str

  # ALGORITMA
	valid = False
	while not valid:
		pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ").lower()
		if (pilihan == 'y'):
			save()
			valid = True
		elif(pilihan == 'n'):
			valid = True
	sys.exit()
# END OF F17