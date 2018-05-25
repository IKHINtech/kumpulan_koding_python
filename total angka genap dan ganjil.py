print('latian-4 soal no 2')
bil = int(input('masukkan angka = '))
jumlah=0
jml=0
for i in range(1,bil+1):
	if i%2==0:
		jumlah=jumlah+1
print('total angka genap',jumlah)
for n in range(1,bil+1):
        if n%2==1:
                jml=jml+1
print('total angka ganjil',jml)
