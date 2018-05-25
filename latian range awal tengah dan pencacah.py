a=int (input ("masukkan nilai awal="))
b=int (input ("masukkan nilai akhir="))
c=int (input ("masukkan pencacah="))

count=0
summ=0
kali = 1
bagi = 1

for i in range (a,b,c):
	print (i, end=' ')
	count=count+1
	summ=summ+1
	kali = kali * 1
	
print ("jumlah perulangan %d kali" %count) 
print ("total penjumlahan bilangan ada %d " %summ)
print ("Jumlah perkalian semua bilangan ada %d " %kali)
