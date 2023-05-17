#dictionary berbentuk scalar (1 dimensi)
m1 = {'nama':'Firda', 'matkul':'Matematika', 'nilai':75}
m2 = {'nama':'Inaya', 'matkul':'Web Dasar', 'nilai':100}
m3 = {'nama':'Bedu', 'matkul':'Agama', 'nilai':59}
m4 = {'nama':'Fawwaz', 'matkul':'DDP', 'nilai':95}

#array associative ( multi dimensi )
ar_nilai = [ m1, m2, m3, m4]

print('----------cetak daftar nilai dengan nested loop--------')
for n in ar_nilai:
    for kolom,data in n.items():   
        #-----cetak data awal------
        print(kolom,':',data)
        nilai = n['nilai']
        #uji kelulusan
        ket = ('Gagal','Lulus')[nilai >= 60]
        #uji grade dan predikat
        if nilai >= 85 and nilai <= 100:
            grade = 'A'
            predikat = 'Memuaskan'
        elif nilai >= 75 and nilai < 85:
            grade = 'B'
            predikat = 'Bagus' 
        elif nilai >= 60 and nilai < 75:
            grade = 'C'
            predikat = 'Cukup'  
        elif nilai >= 30 and nilai < 60:
            grade = 'D'
            predikat = 'Kurang'
        else:
            grade = 'E'
            predikat = 'Buruk' 
    #------cetak data tambahan ket, grade, predikat--------   
    print('Keterangan:',ket,
        '\nGrade:',grade,
        '\nPredikat:',predikat,
        '\n------------------------------'
    )