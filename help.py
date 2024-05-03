from fungsi_sakti import *
import data

def Help(admin):
# F14 - Help
# Akses: Admin dan User
# I.S : Admin terdefinisi sembarang
# F.S : Menampilkan panduan penggunaan aplikasi 

  # KAMUS LOKAL
  # admin : bool

  # ALGORITMA
  Wait()
  if(admin):
    print("""============ HELP ============
F02 - register - Untuk melakukan registrasi user baru
F03 - login - Untuk melakukan login ke dalam sistem
F04 - tambah_game - Untuk menambah game yang dijual pada toko
F05 - ubah_game - Untuk mengubah game pada toko game
F06 - ubah_stok - Mengubah stok sebuah game pada toko dilakukan melalui input ID dan besar perubahan
stok yang ingin dilakukan. 
F07 - list_game_toko - Untuk melihat list game yang dijual pada toko
F11 - search_game_at_store - Untuk mencari game di toko berdasarkan ID, Nama Game, Harga, Kategori
dan Tahun Rilis
F12 - topup - untuk menambahkan saldo kepada User
F16 - save - untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan 
F17 - exit - untuk keluar dari aplikasi              
              """)
        
  else:
    print("""============ HELP ============
F03 - login - Untuk melakukan login ke dalam sistem
F07 - list_game_toko - Untuk melihat list game yang dijual pada toko
F08 - buy_game - untuk memebeli game yang diinginkan pengguna
F09 - list_game - memberikan daftar game yang dimiliki pengguna
F10 - search_my_game - untuk mendapatkan informasi game sesuai dengan query yang
diminta oleh pengguna pada inventory
F11 - search_game_at_store - Untuk mencari game di toko berdasarkan ID, Nama Game, Harga, Kategori
dan Tahun Rilis
F13 - riwayat - untuk melihat riwayat pembelian game yang dilakukan pengguna      
F16 - save - untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan              
F17 - exit - untuk keluar dari aplikasi              
              """)