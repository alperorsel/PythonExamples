# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

galibiyet=0
maglubiyet=0
berabere=0

is_end=False

Seher = " Taş(T) Kağıt(K) veya Makas(M)dan birini seçiniz ya da çıkış yapmak için X e basınız \n "

while True:
    kullanici_choice = input(Seher)
    while kullanici_choice not in [ 'T' , 'K' , 'M' , 'X' ]:
          kullanici_choice = input(Seher)
    if kullanici_choice == 'X' :
        break
    else:
        bilgisayar_choice = random.choice(['T','K','M'])
        if bilgisayar_choice == 'T' :
              el= 'Tas'
              if kullanici_choice == 'K'   and   bilgisayar_choice=='T':
                  print('Kazandın')
                  galibiyet+=1  
              elif  kullanici_choice == 'M'   and   bilgisayar_choice=='T':
                   print('Kaybettin')
                   maglubiyet+=1 
              else :
                  print('Berabere')
                  berabere+=1     
        elif bilgisayar_choice == 'M':
              el= 'Makas'
              if kullanici_choice == 'K'   and   bilgisayar_choice=='M':
                   print('Kaybettin')
                   maglubiyet+=1
              elif  kullanici_choice == 'T'   and   bilgisayar_choice=='M':
                 print('Kazandın')
                 galibiyet+=1
              else:
                  print('Berabere')
                  berabere+=1
              continue    
        else:
              el = 'Kağıt'
              if  kullanici_choice == 'M'   and   bilgisayar_choice=='K':
                   print('Kazandın')
                   galibiyet+=1
                   
              elif  kullanici_choice == 'T'   and   bilgisayar_choice=='K':
                   print('Kaybettin')
                   maglubiyet+=1
              else:
                  print('Berabere')
                  berabere+=1
              continue       
                   
              print('Bilgisayar' + str(el) + 'oynadı')
             
print('Sonuç olarak' + str(maglubiyet) + '' + ' kere kaybettiniz'   + str(galibiyet) + '' +' kere kazandınız'  +  str(berabere) + ' kere berabere kaldınız')
 
                   
                
