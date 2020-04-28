# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os

def calc_hand(hand):
    top= 0
    
    as_olmayan = [kart for kart in hand if kart != 'A']
    aslar = [kart for kart in hand if kart == 'A']
    
    for kart in as_olmayan:
        if kart in 'JQK':
            top += 10
        else:
            top += int(kart)
                
    for kart in aslar:
       if top <=10:
           top +=11
       else:
           top +=1
 
    return top              
                

kartlar=[ '2','3','4','5','6','7','8','9','10','J','K','Q','A'
          '2','3','4','5','6','7','8','9','10','J','K','Q','A'
          '2','3','4','5','6','7','8','9','10','J','K','Q','A'
          '2','3','4','5','6','7','8','9','10','J','K','Q','A'
]
random.shuffle(kartlar)

kurpiye=[]
oyuncu=[]

oyuncu.append(kartlar.pop())
kurpiye.append(kartlar.pop())
oyuncu.append(kartlar.pop())
kurpiye.append(kartlar.pop())

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    
    oyuncu_puan= calc_hand(oyuncu)
    kurpiye_puan= calc_hand(kurpiye)
    
    print('kurpiye kartları:      [{}][?]'.format(kurpiye[0]))
    print('oyuncu kartları[{}] ({})'.format(']['.join(oyuncu), oyuncu_puan))
    
    break