awal=int (input("set nilai awal="))
akhir=int (input("set nilai akhir="))

count=0
summ=0

print ("bilangan antara %d dan %d" %(awal,akhir))

for i in range (awal,akhir+1):
	print (i, end=' ')
	count=count+1
	summ=summ+1
	
print ("bilangan di atas ada %d bilangan" %count)
print ("Jumlah semua bilangan adalah %d" %summ)
