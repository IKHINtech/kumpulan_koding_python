n = int(input('masukkan angka= '))
i = 1
a = 0
for i in range(1, n+1):
        if i%3 == 0:
                print(i,end=' ')
print('merupakan bilangan kelipatan 3')
for i in range(1, n+1):
        if i%3 == 0:
                a = a + 1
print ('jumlah angka kelipatan 3 ada = ',a)
