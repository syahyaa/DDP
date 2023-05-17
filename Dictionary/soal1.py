# Soal 1
# Membuat Dictionary
p1 = {'nama':'Budi' , 'nilai':75 , 'matpel':'Matematika'}
p2 = {'nama':'Dewi' , 'nilai':55 , 'matpel':'Ipa'}
p3 = {'nama':'Ani' , 'nilai':95 , 'matpel':'Ips'}
p4 = {'nama':'Bedu' , 'nilai':30 , 'matpel':'Agama'}
p5 = {'nama':'Ahmad' , 'nilai':83 , 'matpel':'Bahasa Inggris'}

# Membuat List
ar_siswa = [p1, p2, p3, p4, p5]

# Mnggunakan Nested loop
for mahasiswa in ar_siswa:
    nama = mahasiswa['nama']
    matpel = mahasiswa['matpel']
    nilai = mahasiswa['nilai']
   
    #Menggunakan Tuple & List 
    keterangan = ('Lulus','Gagal')[nilai <= 60]

    # IF Multi Kondisi
    if nilai >= 85 and nilai <= 100:
        grade = 'A'
        predikat = 'Memuaskan'
    elif nilai >= 75 and nilai <= 85:
        grade = 'B'
        predikat = 'Bagus'
    elif nilai >= 60 and nilai <= 75:
        grade = 'C'
        predikat = 'Cukup'
    elif nilai >= 30 and nilai <= 60:
        grade = 'D'
        predikat = 'Kurang'
    else:
        grade = 'E'
        predikat = 'Buruk'

    print('\nNama\t\t: ', nama,
        '\nMatpel\t\t: ', matpel,
        '\nNilai\t\t: ', nilai,
        '\nKeterangan\t: ', keterangan,
        '\nGrade\t\t: ', grade,
        '\nPredikat\t: ', predikat,
        '\n___________________________')