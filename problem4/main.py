'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

#input
Harga = 370000
Diskon = 15

#kode disini
Harga_diskon = (Diskon/100)*Harga
Harga_akhir = Harga - Harga_diskon

print(Harga_akhir)