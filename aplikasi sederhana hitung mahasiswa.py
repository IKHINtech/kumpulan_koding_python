matakuliah = input ("Masukkan nama Matakuliah=")
nama = input ("Masukkan Nama Anda=")
nim = input ("Masukakn NIM anda=")
jawaban = "ya"
hitung = 0
while(jawaban == "ya"):
	hitung += 1
	jawaban = input ("ulangi lagi tidak?")
	if jawaban =="ya":
		matakuliah = input ("Masukkan nama Matakuliah=")
		nama = input ("Masukkan Nama Anda=")
		nim = input ("Masukakn NIM anda=")
	continue
print ("total mahasiswa : " + str(hitung))
