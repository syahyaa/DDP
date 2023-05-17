class Gempa:
    # Membuat Variable1
    # lokasi = ''
    # skala = 0
    # Member2 Konstruktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        # self.ket = ket
    # Member3 Method
    def dampak(self):
        if(self.skala < 2): 
            ket = 'Tidak Terasa'
        elif(self.skala >= 2 and self.skala < 4): 
            ket = 'Bangunan Retak'
        elif(self.skala >= 4 and self.skala < 6): 
            ket = 'Bangunan Roboh'
        else : 
            ket = 'Bangunan Roboh dan Berpotensi Tsunami'
        return ket

    def cetak(self):
        print(
            '\nLokasi Gempa\t:', self.lokasi,
            '\nSkala\t\t:', self.skala, 'Richter'
            '\nDampak\t\t:',self.dampak(),
            '\n---------------------------')