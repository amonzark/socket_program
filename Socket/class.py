class sum(object):
    def jumlah(self,a,b): #self = this
        return a+b

a = 3
b = 4
x = sum() #inisialisasi objek dari class
c = x.jumlah(a,b) #pemanggilan method
print(c)