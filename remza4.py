#! /usr/bin/env python3.2
# -*- coding: utf_8 -*-

import re
import random

dsh = """
    __________________________
  _|  __) _ \/  \/  \|_  /|__ |
 |_| | +  __/ /\  /\ \/ /_/ - |
   |_|__\__/_/__\/__\_\___|___|

 (c) 2010 David Samuel Hollands BSc Lond (大卫 塞缪尔 霍兰斯)

 remza is currently a na\u00EFve language generator...
"""
i = len(dsh)
if dsh[:i] + dsh[i:] == dsh: # A useful invariant of slice operations 
    print(dsh)

def eval(gr):
    pass

# gen(S='AB|c', A='Aa|#', B='b|d')
def gen(**grammar):
    print(' Nonterminals: ' + str(list(grammar.keys())))
    for k, v in grammar.items():
        print(' ', k, v.split('|'))

    print(' \n Chuck S in the bag...')
    bag = {'S'}
    lang = set() 
    nonterminal = re.compile("[A-Z]")
    count = 0
    while bag != {} and count < 1000000:
        x = bag.pop() # is arbitary
        if x.islower():
            lang.add(x)
        else:
            y = x[nonterminal.search(x).start(0)]
#            alt = random.choice(grammar[y].split('|'))
            for alt in grammar[y].split('|'):
                bag.add(x.replace(y, alt, 1))
        count = count + 1
#        print(count)

    print('\n{0} Language: {1}\nAfter {0} iterations {2} sentences were generated with {3} sentential forms still in the bag.\nThe size of the bag of sentential forms in memory, in bytes, is {4}.'.format(count, lang, len(lang), len(bag), bag.__sizeof__()))


gen(S='S-S|S*S|a')
