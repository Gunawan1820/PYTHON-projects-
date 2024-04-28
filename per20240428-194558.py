class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul   = judul
        self.penulis = penulis
        self.genre   = genre
        self.status  = status
        
    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.genre}) - Status: {self.status}"
        
class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []
        
    def check_ketersediaan(self):
        if not self.buku.tersedia:
            print(f"Buku {self.buku.judul}' tidak tersedia untuk dipinjam.")
        
    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("Koleksi buku masih kosong.")
            
    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
        print(f"Buku dengan judul '{judul} tidak ditemukan.")
             
    def pinjam_buku(self, judul, anggota):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                if buku.status == " Tersedia ":
                    buku.status = " Dipinjam "
                    anggota.buku_pinjaman.append(buku)

                    #Memperbarui list buku yang dipinjam 
                    for koleksi_buku in self.koleksi_buku:
                        if koleksi_buku.judul == buku.judul:
                            koleksi_buku.status = buku.status

                    print(f"Buku '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
                    return
                else:
                    print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")
                    return
        print(f"Buku dengan judul '{judul}' tidak ditemukan.")
    
class Anggota:
    def __init__(self, nama, ID, alamat=None, nomor_telepon=None):
        self.nama          = nama
        self.ID            = ID
        self.alamat        = alamat
        self.nomor_telepon = nomor_telepon
        self.buku_pinjaman = []
        
    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- Buku Pinjaman {self.nama} --")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")
            
class Catatan_peminjaman:
    def __init__(self, id_buku, id_anggota, tanggal_pinjam, tanggal_kembali):
        self.id_buku         = id_buku
        self.id_anggota      = id_anggota
        self.tanggal_pinjam  = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali          
            
def main():
    # Buat beberapa buku
    buku1 = Buku("Bumi", "Tere Liye", "Fiksi", "Dipinjam")
    buku2 = Buku("Laskar Pelangi","Andrea Hirata", "Fiksi", "Tersedia") 
    buku3 = Buku("Filosofi Terbang", "Dewi Lestari", "Fiksi", "Tersedia")

    # Buat perpustakaan
    perpustakaan = Perpustakaan() 
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])
    
    # Buat anggota
    anggota1 = Anggota("Abi", 12345) 
    anggota2 = Anggota("Agi", 56789)

    # Jalankan program
    
    print("\n-- Menu Perpustakaan --") 
    print("1. Tampilkan Daftar Buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan")
    angka = int(input("Pilih menu : "))
    
    if angka == 1:
        perpustakaan.tampilkan_buku()
    elif angka == 2:
        judul = input("Masukkan judul buku : ")
        perpustakaan.cari_buku(judul)
    elif angka == 3:
        perpustakaan.tampilkan_buku()
        judul = input("Judul buku yang akan dipinjam : ")
        anggota = input("Masukkan nama anggota         : ")
        perpustakaan.pinjam_buku(judul, anggota1)
    elif angka == 4:
        print("Daftar buku yang sudah dipinjam")
        print("1.Filosofi Terbang")
        angka = int(input("pilih berdasarkan angka : "))
        if angka == 1:
            print("Terima kasih sudah mengembalikan bukunya")
        else:
            print("Anda salah memilih")
    else:
        print("Anda salah memilih.")
if __name__ == "__main__":
    main()