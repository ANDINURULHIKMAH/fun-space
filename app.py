def luas_segitiga():
    a = int(input("Masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)
    
luas_segitiga()

def luas_persegi_panjang():
    p = int(input("Masukakan panjang persegi: "))
    l = int(input("Masukkan lebar persegi: "))
    luas = p * l
    print("Luas persegi adalah: ",luas)
    
luas_persegi_panjang()
#menambah rumus baru
def luas_lingkaran():
    r = int(input("Masukkan r: "))
    luas = 3.14 * r * r
    print("Luas", luas)
luas_lingkaran()
