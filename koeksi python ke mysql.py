import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', database='test')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User nama atau password salah")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database tidak ada")
    else:
        print(err)
else:
    #cnx.close()
      print("Koneksi Database Berhasil")
