#! /usr/bin/env python3.2
# -*- coding: utf_8 -*-
import io

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

class Production:
    def __init__(self, lhs, rhs):
        self.lhs = lhs.strip()
        self.alternates = encapsulate_alternates(rhs.split('|')) 

class Alternate:
    def __init__(self, selector_set, rhs):
        self.selector_set = selector_set
        self.rhs = rhs.strip()
            
# Process rhs into Alternate objects (selector_set and string/sentential_form)
# Return a set/ordered list of Alternate objects        
def encapsulate_alternates(list_of_strings):
    alternates = []
    for str in list_of_strings:
        selector_set = str[str.find('{')+1:str.find('}')].split(',')
        rhs = str[str.find('}')+1:].strip()
        alternates.append(Alternate(selector_set, rhs.strip(';')))
    return alternates 

grammar = open('grammar', 'r')
start = grammar.readline().lstrip('start:').strip()

productions = []

for rule in grammar:
    if (rule == '\n'):
        continue
    else:
        y = rule.split('::=')
        productions.append(Production(y[0], y[1]))
        
grammar.close()

output = io.StringIO()
output.write("""#! /usr/bin/env python3.2\n
# -*- coding: utf_8 -*-\n
x = ''\n
input = open('input', 'r+')\n
\n
def get_next_symbol():\n
    next = input.read(1)\n
    while next == ' ':\n
        next = input.read(1)\n
    return next\n 
\n
def main():\n
    global x\n
    x = get_next_symbol()\n
    parse{0}()\n
    if (x == '$'):\n
        print("pass")\n
    else:\n
        print("fail")\n
""".format(start))

for p in productions:
    can_be_nullified = False
    output.write("""
def parse{0}():\n
    global x\n
    """.format(p.lhs))
    i = 0
    for a in p.alternates:
        if (i == 0):
            if (a.rhs == '#'):
                can_be_nullified = True # needs to be refactored here 
            else:
                output.write("""
    if (x == """)
        else:
            if (a.rhs == '#'):
                can_be_nullified = True # needs to be refactored here
            else:
                output.write("""
    elif (x == """)
        i = i + 1
        j = 0
        for s in a.selector_set:
            if (s == ''):
                continue
            output.write("""'{0}'""".format(s.strip())) # the use of strip() here is a temp hack
            if (j == len(a.selector_set) - 1):
                output.write("""):\n""")
            else:
                output.write(""" or x == """) 
            j = j + 1  
        for alpha in a.rhs:
            if (alpha == ' '):
                continue
            if (alpha == '#'):
                can_be_nullified = True # needs to be refactored here
            elif (alpha.isupper()):
                output.write("""
        parse{0}()\n""".format(alpha))
            else:
                output.write("""
        if (x == '{0}'):\n
            x = get_next_symbol()\n
        else:\n
            print("error - parse{1}() - if (x == '{0}')")\n""".format(alpha, p.lhs))
    if (can_be_nullified != True):
        output.write("""
    else:\n
        print('error - can not be directly nullified')\n""")

output.write("""
main()\n""")

contents = output.getvalue()
output.close()
recogniser = open('rec.py', 'w')
recogniser.write(contents)
recogniser.close()
print(' A recogniser has been generated: rec.py\n\n')
