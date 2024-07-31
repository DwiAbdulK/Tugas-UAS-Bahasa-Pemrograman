import math

def luas_persegi(sisi):
    return sisi * sisi
def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari
def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

if __name__ == "__main__":
    print("Pilih bangun datar yang ingin dihitung:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    
    pilihan = int(input("Masukkan pilihan (1-4): "))

    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Luas Persegi: {luas_persegi(sisi)}")
        print(f"Keliling Persegi: {keliling_persegi(sisi)}")

    elif pilihan == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        print(f"Luas Persegi Panjang: {luas_persegi_panjang(panjang, lebar)}")
        print(f"Keliling Persegi Panjang: {keliling_persegi_panjang(panjang, lebar)}")

    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi1 = float(input("Masukkan panjang sisi 1: "))
        sisi2 = float(input("Masukkan panjang sisi 2: "))
        sisi3 = float(input("Masukkan panjang sisi 3: "))
        print(f"Luas Segitiga: {luas_segitiga(alas, tinggi)}")
        print(f"Keliling Segitiga: {keliling_segitiga(sisi1, sisi2, sisi3)}")

    elif pilihan == 4:
        jari_jari = float(input("Masukkan jari-jari: "))
        print(f"Luas Lingkaran: {luas_lingkaran(jari_jari)}")
        print(f"Keliling Lingkaran: {keliling_lingkaran(jari_jari)}")

    else:
        print("Pilihan tidak tersedia. Silakan pilih 1, 2, 3, atau 4.")

