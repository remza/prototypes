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

 remza is currently generating recursive descent recognisers from 'first principles'...
"""
i = len(dsh)
if dsh[:i] + dsh[i:] == dsh: # A useful invariant of slice operations 
    print(dsh)

grammar = open('grammar', 'r+')
for line in grammar:
    print(line, end='')

x = ''
input = open('input', 'r+')

def get_next_symbol():
    next = input.read(1)
    while next == ' ':
        next = input.read(1) 
    return next 

def main():
    global x
    x = get_next_symbol()
    parseS()
    if (x == '$'): 
        print("pass")
    else:
        print("fail")

def parseS():
    global x
    if (x == 'a'):
        if (x == 'a'): 
            x = get_next_symbol()
        else:
            print("error - should terminate - parseS() - if (x == 'a')")
        parseS()
    elif (x == 'd'):
        if (x == 'd'):
            x = get_next_symbol()
        else:
            print("error - should terminate - parseS() - if (x == 'd')")
        parseA()
    elif (x == 'e' or x == 'f' or x == 'b'):
        parseB()
        if (x == 'f'):
            x = get_next_symbol()
        else:
            print("error - should terminate - parseS() - if (x == 'f')")
        parseB()
    else:
        print('error - should terminate - parseS() - x currently is {0}'.format(x)) # for S can not be directly nullified

def parseA():
    global x
    if (x == 'e' or x == 'f'):
        parseC()
        parseB()

def parseB():
    global x
    if (x == 'e' or x == 'f' or x == 'b'):
        parseA()
        if (x == 'b'):
            x = get_next_symbol()
        else:
            print("error - should terminate - parseB() - if (x == 'b')")
        parseB()
    else:
        print('error - should terminate - parseB() - x currently is {0}'.format(x)) # for B can not be directly nullified 

def parseC():
    global x
    if (x == 'e'):
        if (x == 'e'):
            x = get_next_symbol()
        else:
            print("error - should terminate - parseC() - if (x == 'e')")
    elif (x == 'f'):
        if (x == 'f'):
            x = get_next_symbol()
        else:
            print("error - should terminate - parseC() - if (x == 'f')")
    else:
        print('error - should terminate - parseC() - x currently is {0}'.format(x)) # for C can not be directly nullified
    
main()
