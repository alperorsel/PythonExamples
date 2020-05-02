# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def calc_hand(hand):

    top= 0
    
    for i in hand:
        if i not in special_cards:
            top += int(i)
        elif i != "A":
            top += 10
        else:
            if top <= 10:
                top += 11
            else:
                top += 1

    return top              


special_cards = ["J", "K", "Q", "A"]               

kartlar=[ '2','3','4','5','6','7','8','9','10','J','K','Q','A',
          '2','3','4','5','6','7','8','9','10','J','K','Q','A',
          '2','3','4','5','6','7','8','9','10','J','K','Q','A',
          '2','3','4','5','6','7','8','9','10','J','K','Q','A',
]


random.shuffle(kartlar)

kurpiye = []
oyuncu = []

oyuncu.append(kartlar.pop())
kurpiye.append(kartlar.pop())
oyuncu.append(kartlar.pop())
kurpiye.append(kartlar.pop())

while True:

    oyuncu_puan = calc_hand(oyuncu)
    kurpiye_puan = calc_hand(kurpiye)

    print(f"oyuncu kartları: {oyuncu}, puan: {oyuncu_puan}")
    print(f"kurpiye kartları: {kurpiye[0]} '?', puan: {kurpiye_puan}")

    if oyuncu_puan == 21:
        print('Kazandınız')
    elif kurpiye_puan == 21:
        print('Kaybettiniz')
    else:
	    giris1 = input('devam etmek ister misiniz?')

    while giris1 == 'hayır' and kurpiye_puan < 21:
        print(f"oyuncu kartları: {oyuncu}, puan: {oyuncu_puan}")
        print(f"kurpiye kartları: {kurpiye}, puan: {kurpiye_puan}")
        if  kurpiye_puan > oyuncu_puan:
            print('kurpiye kazandı')
            break
        elif kurpiye_puan > 21:
            print('kazandınız')
            break
        elif  kurpiye_puan < oyuncu_puan:
            print('kazandınız')
            break
    break
 
        
           
