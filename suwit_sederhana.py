# suwit sederhana python
from pdb import Restart


def suwitSimple():
    import random
    print("pilih huruf a untuk Batu, pilih huruf b untuk kertas, pilih huruf c untuk gunting")
    print("a = batu")
    print("b = kertas")
    print("c = gunting")
    print("")
    x = input("Masukkan a, b atau c : ")
    print("")
    if x == 'a':
        x = 'Batu'
    elif x == 'b':
        x = 'Kertas'
    elif x == 'c':
        x = 'Gunting'
    else:
        x = '0'
        print("Input Salah")
        suwitSimple()
        Restart


    y = random.random()
    if y <= 0.33:
        y = 'Batu'
        print(y)
    elif y <= 0.66:
        y = 'Kertas'
        print(y)
    else:
        y = 'Gunting'
        print(y) 

    if x == y:
        hasil = 'Seri'
    elif x == 'Batu' and y == 'Kertas':
        hasil = 'Anda Kalah'
    elif x == 'Batu' and y == 'Gunting':
        hasil = 'Anda Menang'
    elif x == 'Kertas' and y == 'Batu':
        hasil = 'Anda Menang'
    elif x == 'Kertas' and y == 'Gunting':
        hasil = 'Kalah'
    elif x == 'Gunting' and y == 'Batu':
        hasil = 'kalah'
    elif x == 'Gunting' and y == 'Kertas':
        hasil = 'Menang'
    else:
        suwitSimple()

    print("Anda Memilih : ",x)
    print("Bot memilih : ",y)
    print("hasil : ",hasil)

suwitSimple()
