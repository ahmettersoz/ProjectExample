from __future__ import division


while True:

    def toplama_islemi():
        girdi1t=input("Ilk sayiyi girin: ")
        girdi2t=input("Ikinci sayiyi girin: ")
        sonuct=girdi1t+girdi2t
        print "Sonuc :" , sonuct
        print
    def cikarma_islemi():
        girdi1c=input("Ilk sayiyi girin: ")
        girdi2c=input("Ikinci sayiyi girin: ")
        sonucc=girdi1c-girdi2c
        print "Sonuc :" , sonucc
        print
    def carpma_islemi():
        girdi1ca=input("Ilk sayiyi girin: ")
        girdi2ca=input("Ikinci sayiyi girin: ")
        sonucca=girdi1ca*girdi2ca
        print "Sonuc :" , sonucca
        print
    def bolme_islemi():
        girdi1bo=input("Ilk sayiyi girin: ")
        girdi2bo=input("Ikinci sayiyi girin: ")
        sonucbo=girdi1bo/girdi2bo
        print "Sonuc :" , sonucbo
        print

    print ("Toplama Islemi (1)")
    print ("Cikarma Islemi (2)")
    print ("Carpma Islemi (3)")
    print ("Bolme Islemi (4)")
    print ("Programdan cikmak icin (5)")
    print ("------------------")
    islemno=input("Islem numarasini girin: ")

    if islemno == 1:
        toplama_islemi()
    elif islemno == 2:
        cikarma_islemi()
    elif islemno == 3:
        carpma_islemi()
    elif islemno == 4:
        bolme_islemi()
    elif islemno == 5:
        break
    else:
        print ("Islem numarasi gecersiz")
