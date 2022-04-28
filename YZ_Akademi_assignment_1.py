#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:08:46 2022

@author: yasin
"""

import sys

inp_Alice = list(map(int, input().split()))

inp_Bob = list(map(int, input().split()))

if  len(inp_Alice) & len(inp_Bob) == 3:
    
    Output = [0,0]
    
    for i in range(0,3):
        
        if 0 <= inp_Alice[i] <= 100:
            pass
        else:
            sys.exit("Alice's elements should be on a scale from 0 to 100")
        
        if 0 <= inp_Bob[i] <= 100:
            pass
        else:
            sys.exit("Bob's elements should be on a scale from 0 to 100")
        
        
        if inp_Alice[i] > inp_Bob[i]:        # Alice receives 1 point.

            Output[0] = Output[0]+1 
    
        elif inp_Alice[i] < inp_Bob[i]:      # Bob receives 1 point.
    
            Output[1] = Output[1]+1
        else:
                pass                     # Nobody receives 1 point.

elif (len(inp_Alice)!= 3) and (len(inp_Bob) != 3): 
    sys.exit("Alice's or Bob's ratings length should be 3")

elif len(inp_Alice) !=3:
     sys.exit("Alice's ratings length should be 3")

elif len(inp_Bob) !=3:
     sys.exit("Bob's ratings length should be 3")
else:
    pass

    print(Output[0],Output[1])

