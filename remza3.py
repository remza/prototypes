#! /usr/bin/env python3.2
# -*- coding: utf_8 -*-

import re
import random

dsh = """
    __________________________
  _|  __) _ \/  \/  \|_  /|__ |
 |_| | +  __/ /\  /\ \/ /_/ - |
   |_|__\__/_/__\/__\_\___|___|

 (c) 2010 David S. Hollands BSc Lond

 remza is currently a na\u00EFve language generator...
"""
i = len(dsh)
if dsh[:i] + dsh[i:] == dsh: # A useful invariant of slice operations 
    print(dsh)

def eval(gr):
    pass

# gen(S='AB|c', A='Aa|#', B='b|d')
def gen(**grammar):
#    print('Nonterminals: ' + str(list(grammar.keys())))
    for k, v in grammar.items():
        print(' ', k, v.split('|'))

    print(' \n Chuck S in the bag...')
    bag = {'S'}
    lang = set() 
    nonterminal = re.compile(r"[A-Z]")
    count = 0
    while bag != {} and count < 10:
        x = bag.pop()
        if nonterminal.search(x):
            y = x[nonterminal.search(x).start(0)]
            print(y)
            z = re.sub('{0}'.format(y), x, random.choice(grammar[y].split('|')), count=1)
            print(z)
            bag.add(z)
        else:
            lang.add(x)
        print('Language:' + str(lang) + ' Bag: ' + str(bag))
        count = count + 1

gen(S='AB|c', A='Aa|#', B='b|d')
