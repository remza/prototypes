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
#    x = grammar['S'] 
#    start_symbol = True 
    while bag != {} and count < 10:
#        if not start_symbol:
#            x = bag.pop()
#        else:
#            start_symbol = False
        x = bag.pop()
        for v in nonterminal.match(x).group():
            alternates = grammar[v].split('|')
            print('Alternates ' + str(alternates) + ' of {0}'.format(x))
            for i in range(len(alternates)): 
                if nonterminal.search(alternates[i]):
#                for j in sentential_forms[i]:
#                    print(i, j)
#                    if nonterminal.match(j):
#                        print('Grammar: ' + grammar[j])
                        y = nonterminal.match(alternates[i]).group()
                        alternate = random.choice(grammar[y].split('|'))
                        print('Choice: ' + alternate + '\nBefore: ' + alternates[i])
                        z = re.compile('[{0}]'.format(y))
                        derivation = z.sub(alternate, alternates[i])
                        print('After:  ' + derivation)
                        bag.add(derivation)
#                    else:
#                        print('{0} is a terminal'.format(j))
                else:
                    lang.add(alternates[i])
        print('Language:' + str(lang) + ' Bag: ' + str(bag))
        count = count + 1

gen(S='AB|c', A='Aa|#', B='b|d')
