#Membuat Dictionary
p1 = {'nama':'Budi' , 'produk': 'TV' ,  'jumlah': 3}
p2 = {'nama':'Ani' , 'produk': 'AC' , 'jumlah': 4}
p3 = {'nama':'Siti' , 'produk': 'Kulkas' , 'jumlah': 2}
p4 = {'nama':'Dewi' , 'produk': 'AC' , 'jumlah': 5}
p5 = {'nama':'Andi' , 'produk': 'Kulkas' , 'jumlah': 7}
p6 = {'nama':'Dedi' , 'produk': 'AC' , 'jumlah': 1}
p7 = {'nama':'Sri' , 'produk': 'TV' , 'jumlah': 4}

#Membuat List
ar_pelanggan =[p1, p2, p3, p4, p5, p6, p7]

#Membuat Nested Loop
for pelanggan in ar_pelanggan:
  for pel in pelanggan:
#harga satuan
    if pelanggan ['produk'] == 'TV':
        harga_satuan =5000000
    elif pelanggan ['produk'] == 'AC':
        harga_satuan =6000000
    else:
        harga_satuan =700000

    #harga kotor 
    harga_kotor = pelanggan['jumlah'] * harga_satuan

    #diskon
    if pelanggan['jumlah'] >=3 and pelanggan ['produk'] == 'kulkas':
      diskon =0.2 * harga_kotor
    else:
      diskon =0.05 * harga_kotor
      
    #PPN
    ppn = 0.11 * (harga_kotor - diskon)
    
    #harga bayar
    harga_bayar = (harga_kotor + ppn) - diskon
    print(pel,':',pelanggan[pel])
    
  print('harga satuan\t:',harga_satuan,
      '\nharga kotor\t:',harga_kotor,
      '\ndiskon\t\t:',diskon,
      '\nPPN\t\t\t:',ppn,
      '\nharga bayar\t:',harga_bayar,
      '\n' '\n')