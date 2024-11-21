print('---- celcius ----')
def celcius_ke_fahrenheit(celcius):
  """Mengkonversi suhu dari Celcius ke Fahrenheit.

  Args:
    celcius: Suhu dalam Celcius.

  Returns:
    Suhu dalam Fahrenheit.
  """

  fahrenheit = (celcius * 9/5) + 32
  return fahrenheit

# Contoh penggunaan:
print(celcius_ke_fahrenheit(0))  # Output: 32.0
print(celcius_ke_fahrenheit(100)) # Output: 212.0
print('-' * 20)
print()

print('---- bilangan genap ----')
def is_genap(bilangan):
  """Mengecek apakah sebuah bilangan adalah genap.

  Args:
    bilangan: Bilangan bulat yang akan dicek.

  Returns:
    True jika bilangan genap, False jika ganjil.
  """

  return bilangan % 2 == 0

# Contoh penggunaan:
print(is_genap(4))  # Output: True
print(is_genap(7))  # Output: False
print()

print('---- nilai kelulusan ----')
def nilai(skor):
  """Menentukan status kelulusan berdasarkan skor ujian.

  Args:
    skor: Nilai ujian siswa.

  Returns:
    "Lulus" jika skor >= 80, "Gagal" jika tidak.
  """

  if skor >= 80:
    return "Lulus"
  else:
    return "Gagal"

# Contoh penggunaan:
print(nilai(80))  # Output: Lulus
print(nilai(60))  # Output: Gagal
print()

print('---- bilangan ganjil ----')
def bilangan_ganjil(batas):
  """Menampilkan bilangan ganjil dari 1 hingga batas.

  Args:
    batas: Batas atas bilangan ganjil yang akan ditampilkan.
  """

  for i in range(1, batas+1, 2):
    print(i, end=" ")

# Contoh penggunaan:
bilangan_ganjil(20)  # Output: 1 3 5 7 9 11 13 15 17 19
