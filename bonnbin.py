class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak ):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def cetak (self):
        print (self.nama, "memakan", self.makanan, ", hidup di", self.hidup, ", dan berkembang biak dengan cara", self.berkembang_biak)
        print()
        
        
class badak(animal):
    def tempel(self):
        print("badak adalah hewan berkaki 4")

    def __init__(self, nama, makan, hidup, berkembang_biak, jumlah_kaki):
        super().__init__(nama, makan, hidup, berkembang_biak)
        self.jumlah_kaki = jumlah_kaki
        
    def wkwk(self):
        print ("nama hewan: ",self.nama)
        print ("nama makananya: ",self.makanan)
        print ("hidupnya di: ",self.hidup)
        print ("cara berkembang biaknya: ",self.berkembang_biak)
        print ("jumlah kaki: ",self.jumlah_kaki)
        print()
        
       
class ikan(animal):
    def ayo(self):
        print("ikan adalah hewan yang hidup di air")
        
    def __init__(self, nama, makan, hidup, berkembang_biak, masak):
        super().__init__(nama, makan, hidup, berkembang_biak)
        self.masak = masak
        
    def ea(self):
        print ("nama hewan: ",self.nama)
        print ("nama makananya: ",self.makanan)
        print ("hidupnya di: ",self.hidup)
        print ("cara berkembang biaknya: ",self.berkembang_biak)
        print ("paling cocok dimasak dengan: ",self.masak)
        print()
        
    
        
class ular(animal):
    def gasaja(self):
        print("Ular adalah hewan melata")
    
    def __init__(self, nama, makan, hidup, berkembang_biak,  bertahan):
        super().__init__(nama, makan, hidup, berkembang_biak)
        self.bertahan = bertahan
        
    def apa(self):
        print ("nama hewan: ",self.nama)
        print ("nama makananya: ",self.makanan)
        print ("hidupnya di: ",self.hidup)
        print ("cara berkembang biaknya: ",self.berkembang_biak)        
        print ("bertahan hidup dengan: ",self.bertahan)        

    
        
        
x = animal ("kanguru","daun","gurun","melahirkan")
x.cetak()

y = badak ("badak","daun","ujung kulon","melahirkan","4")
y.tempel()
y.wkwk()

z = ikan ("ikan","pelet","air","bertelur","padang")
z.ayo()
z.ea()

o = ular ("ular","daging","semak-semak","melahirkan dan bertelur","bisa")
o.gasaja()
o.apa()