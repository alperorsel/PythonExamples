# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os


def calc_hand(hand):

    handval = 0
    
    for i in hand:
        if i not in special_cards:
            handval += int(i)
        elif i != "A":
            handval += 10
        else:
            if handval <= 10:
                handval += 11
            else:
                handval += 1

    return handval              


special_cards = ["J", "K", "Q", "A"]               

cards=[ '2','3','4','5','6','7','8','9','10','J','K','Q','A',
          '2','3','4','5','6','7','8','9','10','J','K','Q','A',
          '2','3','4','5','6','7','8','9','10','J','K','Q','A',
          '2','3','4','5','6','7','8','9','10','J','K','Q','A',
]


random.shuffle(cards)

dealer = []
player = []

player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())

while True:

    player_points = calc_hand(player)
    dealer_points = calc_hand(dealer)

    print(f"player's cards: {player}, points: {player_points}")
    print(f"dealer's cards: {dealer[0]} '?', points: {dealer_points}")

    if player_points == 21:
        print('you win')
    elif dealer_points == 21:
        print('you lose')
    else:
	    answer1 = input('devam etmek ister misiniz?')

    while answer1 == 'hayır':
        print(f"player's cards: {player}, points: {player_points}")
        print(f"dealer's cards: {dealer}, points: {dealer_points}")
        if dealer_points > 21:
            print('you win')
            break
        elif  dealer_points > player_points:
            print('you lose')
            break
        else:
            dealer.append(cards.pop())
            dealer_points = calc_hand(dealer)

                    
    break