from fungsi_sakti import *

def readAllCSV(address=''):
# Fungsi untuk membaca seluruh file csv yang terdapat dan membuat semua data array global supaya dapat dibaca dan dimanipulasi pada file module lain

	# KAMUS LOKAL
	# user, game, kepemilikan, riwayat : array of array of string
	# address : char

	# ALGORITMA
	global user
	global game
	global kepemilikan
	global riwayat
	
	address += '/'
	
	user = readCSV(address + 'user.csv')
	game = readCSV(address +'game.csv')
	kepemilikan = readCSV(address +'kepemilikan.csv')
	riwayat = readCSV(address +'riwayat.csv')