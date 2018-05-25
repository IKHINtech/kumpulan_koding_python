awal=int (input("set nilai awal="))
akhir=int (input("set nilai akhir="))
pecacahan=int (input("masukan pencacahan="))

count=0
sun=0
kali=1

print ("bilangannn antara %d dan %d %(awal,akhir))

for i in range (awal,akhir+1):
	print (i, end=' ')
	count=count+1
	sum=sum+1
	
print ("bilangan di atas ada %d bilangan" %count)
print ("jumlah semua bilangan adalah %d" %sum)
print ("total perkalian bilangan diatas adalah %d" %kali)
