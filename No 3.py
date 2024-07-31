class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Toko:
    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self, nama, harga, stok):
        barang = Barang(nama, harga, stok)
        self.daftar_barang.append(barang)
        print(f"Barang '{nama}' telah ditambahkan.")

    def tampil_barang(self):
        if not self.daftar_barang:
            print("Tidak ada barang yang tersedia.")
        else:
            for idx, barang in enumerate(self.daftar_barang):
                print(f"{idx + 1}. Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}")

    def delete_barang(self, nama):
        for barang in self.daftar_barang:
            if barang.nama == nama:
                self.daftar_barang.remove(barang)
                print(f"Barang '{nama}' telah dihapus.")
                return
        print(f"Barang dengan nama '{nama}' tidak ditemukan.")

    def cari_barang(self, nama):
        for barang in self.daftar_barang:
            if barang.nama == nama:
                print(f"Barang ditemukan: Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}")
                return
        print(f"Barang dengan nama '{nama}' tidak ditemukan.")

    def hitung_pembelian(self, nama, jumlah):
        for barang in self.daftar_barang:
            if barang.nama == nama:
                if barang.stok >= jumlah:
                    total_harga = jumlah * barang.harga
                    barang.stok -= jumlah
                    print(f"Total harga untuk {jumlah} {nama}: {total_harga}")
                    print(f"Sisa stok {nama}: {barang.stok}")
                else:
                    print(f"Stok {nama} tidak mencukupi. Stok tersedia: {barang.stok}")
                return
        print(f"Barang dengan nama '{nama}' tidak ditemukan.")

def menu():
    toko = Toko()
    while True:
        print("Menu input data barang:")
        print("1. Input data barang")
        print("2. Tampil data barang")
        print("3. Delete data barang")
        print("4. Mencari data barang")
        print("5. Hitung jumlah pembelian")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            nama = input("Masukkan nama barang: ")
            harga = float(input("Masukkan harga barang: "))
            stok = int(input("Masukkan stok barang: "))
            toko.tambah_barang(nama, harga, stok)
        elif pilihan == '2':
            toko.tampil_barang()
        elif pilihan == '3':
            nama = input("Masukkan nama barang yang ingin dihapus: ")
            toko.delete_barang(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama barang yang ingin dicari: ")
            toko.cari_barang(nama)
        elif pilihan == '5':
            nama = input("Masukkan nama barang yang ingin dibeli: ")
            jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
            toko.hitung_pembelian(nama, jumlah)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    menu()