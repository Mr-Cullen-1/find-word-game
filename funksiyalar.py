# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:08:22 2024

@author: Jacob

Topic: So'z topish

Funksiyalar

"""

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in  user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    print("\nKeling so'z topish o'yinini o'ynaymiz!",
          "\nQoidalar bilan tanishtiraman: ",
          "\n> Men bir so'z o'ylayman siz uni topasiz!",
          "\n> Barcha so'zlar 'KIRIL' alifbosida!")
    
    word = get_word()
    word_letters = set(word)
    user_letters = ''

    print(f"\nMen {len(word)} xonali so'z o'yladim. Topa olasizmi?")
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"\nShu vaqtgacha kiritgan harflaringiz > {user_letters}")
        
        letter = input("Xarf kiriting >>> ").upper()
        if letter in user_letters:
            print("\nBu xarfni avval kiritgansiz, boshqa harf kiriting!")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} xarfi to'g'ri!")
        else:
            print("\nBunday xarf yo'q!")
        user_letters += letter
    print(f"\n >>> Tabriklayman! Siz {word} so'zini {len(user_letters)}ta urunishda topdingiz!")
        

play()