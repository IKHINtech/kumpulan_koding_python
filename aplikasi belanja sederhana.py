b = int(input('banyak buah = '))
hitung = 0
jumblnj = 0
for N in range (b):
	print('buah ke-',N+1)
	hitung += 1
	bnybw = int(input('banyak buah yang di beli = '))
	hrg = int(input('masukkan harga ke = '))
	ttlharg = bnybw * hrg
	jumblnj = jumblnj + ttlharg
	ttlharg = ttlharg
	print('total harga : ',ttlharg)
print('total pembelian = %s' % hitung)
print('jumlah belanja = %s' % jumblnj)
