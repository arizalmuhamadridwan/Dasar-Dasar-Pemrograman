def profil(nama, alamat, jk, umur, hoby):
    print("nama saya", nama)
    print("alamat saya", alamat)
    print("jenis kelamin saya", jk)
    print("umur saya", umur)
    print("hoby saya", hoby)

profil("arizal", "bogor", "laki-laki", "23", "game")

def nilai (a):

    if (a <= 60):
        print ("gagal")
    elif (a >= 61 and a <= 70):
        print ("baik")
    elif (a >= 71 and a <= 80):
        print ("sangat baik")
    elif (a >= 81 and a <= 100):
        print ("istimewa")
    else:
        print ("masukan nilai yang benar")
    
nilai(70)


def angka_ganjil(c):
    for i in range(1, 101, 2):
        print(i)

angka_ganjil(100)