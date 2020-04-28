# !/usr/bin/env python
# -*- coding: utf-8 -*-


kullaniciadi=('kingmami9')
sifre=('adamol026')
dogru1=('bir')
devam1=('evet')
giris1=input(' Kullanıcı adı: ')
sifre1=input(' Sifre: ')

a = giris1
a1 = kullaniciadi
b = sifre1 
b1 = sifre

if a==a1 and b==b1:
     print('Oyunumuza hosgeldiniz secmek istediginiz yolu secerek hikayeye yon verin \n')
     print('uzak bi diyarda kerem kırlı karanliklarin efendisi olarak yasamaktaydi \n ')
     print('kereme bir şey yapmak lazım \n bir)keremi Sikeyim \n iki)keremi sikmeyeyim \n ')
     userin2=input(' ona ne yapacaksin ')
     c=len(userin2)
     c1=len(dogru1)
     if(c==c1):
         print('dogru bildiniz \n')
         print('devam etmek ister misiniz ? \n ')
         alper=input('giriniz')
         d=len(devam1)
         if(alper==d):
             print('banane')
         else:
             print('banane aq!')
     else:
         print('büyü')
else:
     print('Sifreniz Yanlis')
