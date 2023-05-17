# Data Mahasiswa
nim = int(input('Nim Mahasiswa: '))
nama = str(input('Nama Mahasiswa: '))
nilai = float(input('Nilai Mahasiswa: '))

m1 = {'nim' : nim, 'nama' : nama, 'nilai' : nilai}

nim = int(input('Nim Mahasiswa: '))
nama = str(input('Nama Mahasiswa: '))
nilai = float(input('nNlai Mahasiswa: '))

m2 = {'nim' : nim, 'nama' : nama, 'nilai' : nilai}

nim = int(input('Nim Mahasiswa: '))
nama = str(input('Nama Mahasiswa: '))
nilai = float(input('Nilai Mahasiswa: '))

m3 = {'nim' : nim, 'nama' : nama, 'nilai' : nilai}

nim = int(input('Nim Mahasiswa: '))
nama = str(input('Nama Mahasiswa: '))
nilai = float(input('Nilai Mahasiswa: '))

m4 = {'nim' : nim, 'nama' : nama, 'nilai' : nilai}

nim = int(input('Nim Mahasiswa: '))
nama = str(input('Nama Mahasiswa: '))
nilai = float(input('Nilai Mahasiswa: '))

m5 = {'nim' : nim, 'nama' : nama, 'nilai' : nilai}

nilai_mahasiswa = [m1, m2, m3, m4, m5]

for mahasiswa in nilai_mahasiswa:
  nim = mahasiswa['nim'];
  nama = mahasiswa['nama'];
  nilai = mahasiswa['nilai'];

  # Keterangan Lulus atau Tidak
  # Keterangan, Grade, Dan Predikat
  if mahasiswa['nilai'] >= 85 and mahasiswa['nilai'] <= 100:
    grade = 'A';
    keterangan = 'Lulus';
    predikat = 'Memuaskan';
  elif mahasiswa['nilai'] >= 75 and mahasiswa['nilai'] <=85:
    grade = 'B';
    keterangan = 'Lulus';
    predikat = 'Bagus'
  elif mahasiswa['nilai'] >= 60 and mahasiswa['nilai'] <= 75:
    grade = 'C'
    keterangan = 'Lulus';
    Predikat = 'Cukup'
  elif mahasiswa['nilai'] >= 30 and mahasiswa['nilai'] <= 60:
    grade = 'D';
    keterangan = 'Gagal';
    predikat = 'Kurang'
  elif mahasiswa['nilai'] >= 0 and mahasiswa['nilai'] <= 30:
    grade = 'E';
    keterangan = 'Gagal';
    predikat = 'Buruk'
  else:
    grade = ''

  print('Nim: %s'
      '\nNama: %s'
      '\nNilai: %.2f'
      '\nKeterangan: %s'
      '\nGrade: %s'
      '\nPredikat: %s' 
      '\n \n'
      %(nim,nama,nilai,keterangan,grade,predikat))