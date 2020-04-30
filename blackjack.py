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

turn_count = 0

while turn_count >= 0:

    player_points = calc_hand(player)
    dealer_points = calc_hand(dealer)

    print(f"player's cards: {player}, points: {player_points}")

    if turn_count == 0:
        print(f"dealer's cards: {dealer[0]} '?', points: {dealer_points}")
    else:
        print(f"dealer's cards: {dealer}, points: {dealer_points}")

    if player_points == 21:
        print('you win')
        answer1 = 0
    elif dealer_points == 21:
        print('you lose')
        answer1 = 0
    elif player_points > 21:
        print("you lose")
        answer1 = 0
    elif dealer_points > 21:
        print("you win")
        answer1 = 0
    else:
	    answer1 = input('devam etmek ister misiniz?\n>')

    if answer1 == 'hayır':
    
        while True:
            
            if dealer_points <= player_points:
                dealer.append(cards.pop())
                dealer_points = calc_hand(dealer)

            print(f"player's cards: {player}, points: {player_points}")
            print(f"dealer's cards: {dealer}, points: {dealer_points}")

            if dealer_points > 21:
                print('you win')
                break
            elif  dealer_points > player_points:
                print('you lose')
                break
            else:
                continue
                
    if answer1 == 'evet':
        turn_count += 1
        player.append(cards.pop())
        
        if dealer_points <= player_points:
            dealer.append(cards.pop())
        
        continue                    
    break