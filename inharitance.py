class manusia:
    def __init__(self, fnama, lnama ):
        self.fnama = fnama
        self.lnama = lnama
        
    def cetak (self):
        print ("Nama saya adalah ", self.fnama , self.lnama)
        
class staff(manusia):
    def bekerja(self):
        print("Saya pekerja keras")
        
        
class pelajar(manusia):
    def __init__ (self, fnama, lnama, prodi, angkatan):
        super().__init__(fnama, lnama)
        self.prodi = prodi
        self.angkatan = angkatan
        
    def cetak(self):
        super().cetak()
        print("saya mahaiswa angkatan", self.angkatan, "dengan prodi", self.prodi)
        
    def belajar(self):
        print("saya adalah pelajar")

# objek manusia
x = manusia("nada","indah")
x.cetak()

#objek staf
y = staff("dedi","drajat")
y.cetak()
y.bekerja()

#objek belajar
danu = pelajar("danu","setiawan","sistem informasi",2023)
danu.cetak()
danu.belajar()
        