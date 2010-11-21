#! /usr/bin/env python3.2

# -*- coding: utf_8 -*-

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

            print("error - parseS() - if (x == 'a')")

        parseS()

    elif (x == 'd'):

        if (x == 'd'):

            x = get_next_symbol()

        else:

            print("error - parseS() - if (x == 'd')")

        parseA()

    elif (x == 'e' or x == 'f' or x == 'b'):

        parseB()

        if (x == 'f'):

            x = get_next_symbol()

        else:

            print("error - parseS() - if (x == 'f')")

        parseB()

    else:

        print('error - can not be directly nullified')

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

            print("error - parseB() - if (x == 'b')")

        parseS()

    else:

        print('error - can not be directly nullified')

def parseC():

    global x

    
    if (x == 'e'):

        if (x == 'e'):

            x = get_next_symbol()

        else:

            print("error - parseC() - if (x == 'e')")

    elif (x == 'f'):

        if (x == 'f'):

            x = get_next_symbol()

        else:

            print("error - parseC() - if (x == 'f')")

    else:

        print('error - can not be directly nullified')

main()
