# Soal 2
nama = str(input('Masukkan Nama: '))
jabatan = str(input('Masukkan Jabatan: '))
agama = str(input('Masukkan Agama: '))
status = str(input('Masukkan Status: '))

p1 = {'Nama':nama, 'Jabatan':jabatan, 'Agama':agama, 'Status':status}

nama = str(input('Masukkan Nama: '))
jabatan = str(input('Masukkan Jabatan: '))
agama = str(input('Masukkan Agama: '))
status = str(input('Masukkan Status: '))

p2 = {'Nama':nama, 'Jabatan':jabatan, 'Agama':agama, 'Status':status}

nama = str(input('Masukkan Nama: '))
jabatan = str(input('Masukkan Jabatan: '))
agama = str(input('Masukkan Agama: '))
status = str(input('Masukkan Status: '))

p3 = {'Nama':nama, 'Jabatan':jabatan, 'Agama':agama, 'Status':status}

nama = str(input('Masukkan Nama: '))
jabatan = str(input('Masukkan Jabatan: '))
agama = str(input('Masukkan Agama: '))
status = str(input('Masukkan Status: '))

p4 = {'Nama':nama, 'Jabatan':jabatan, 'Agama':agama, 'Status':status}

nama = str(input('Masukkan Nama: '))
jabatan = str(input('Masukkan Jabatan: '))
agama = str(input('Masukkan Agama: '))
status = str(input('Masukkan Status: '))

p5 = {'Nama':nama, 'Jabatan':jabatan, 'Agama':agama, 'Status':status}

ini_karyawan = [p1, p2, p3, p4, p5]

# Data Pegawai
for karyawan in ini_karyawan:
    nama = karyawan ['Nama']
    jabatan = karyawan ['Jabatan']
    agama = karyawan ['Agama']
    status = karyawan ['Status']

    # Gaji Pegawai
    if karyawan['Jabatan'] == 'manager':
        gaji_pokok = 15000000
    elif karyawan['Jabatan'] == 'asisten manager':
        gaji_pokok = 10000000
    elif karyawan['Jabatan'] == 'supervisor':
        gaji_pokok = 7000000
    else:
        gaji_pokok = 4000000

    # Tunjangan Jabatan
    tunjangan_jabatan = 0.3 * gaji_pokok

    # Tunjangan Keluarga
    if karyawan['Status'] == 'menikah':
        tunjangan_keluarga = 0.1 * gaji_pokok
    else:
        tunjangan_keluarga = 0

    # Gaji Kotor
    gaji_kotor = gaji_pokok + tunjangan_jabatan +tunjangan_keluarga

    # Zakat
    if karyawan ['Agama'] == 'islam' and gaji_kotor >= 7000000:
        zakat = 0.025 * gaji_kotor
    else:
        zakat = 0

    # Gaji Bersih
    gaji_bersih = gaji_kotor - zakat

    print('Nama\t\t\t: %s'
        '\nJabatan\t\t\t: %s'
        '\nAgama\t\t\t: %s'
        '\nStatus\t\t\t: %s'
        '\nGaji Pokok\t\t: %i'
        '\nTunjanngan Jabatan\t: %i'
        '\nTunjangan Keluarga\t: %i'
        '\nGaji Kotor\t\t: %i'
        '\nZakat\t\t\t: %i'
        '\nGaji Bersih\t\t: %i'
        '\n___________________________'
        %(nama,jabatan,agama,status,gaji_pokok,tunjangan_jabatan,tunjangan_keluarga,gaji_kotor,zakat,gaji_bersih))