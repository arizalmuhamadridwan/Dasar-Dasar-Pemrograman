kendaraan =["vario 150", "motor", "150cc", "hitam", "dua"]
print(kendaraan)

kendaraan =["vario 150", "motor", "150cc", "hitam", "dua"]
kendaraan.append("24.570.000") 
kendaraan.append("matic") 
print(kendaraan)

kendaraan =["vario 150", "motor", "150cc", "hitam", "dua"]
kendaraan.append("24.570.000") 
kendaraan.append("matic")
kendaraan.insert(2, "honda")
print(kendaraan)


print ("""
permainan menghitung bangun datar
pilih angka untuk menghitung
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
""")
pilihan= int(input("masukan pilihan"))
match pilihan:
    case 1:
        print("kamu memilih angka 1 untuk menghitung luas persegi")
        sisi=int(input("masukan sisi:"))
        luas=sisi*sisi
        print("luas persegi dengan sisi",sisi,"adalah",luas)
    case 2:
        print("kamu memilih angka 2 untuk menghitung luas lingkaran")
        r=float(input("masuk jari jari lingkaran:"))
        luas1=3.14*r*r
        print("luas lingkaran dengan jari jari",r,"adalah",int(luas1))
    case 3:
        print("kamu memilih angka 3 untuk menghitung luas segitiga")
        alas=int(input("masukan alas segitiga:"))
        tinggi=int(input("masukan tinggi segitiga:"))
        luas3=1/2*alas*tinggi
        print("luas segitiga dengan alas",alas,"dan tinggi",tinggi,"adalah",int(luas3))
    case 4:
        print("kamu salah memasukan pilihan")