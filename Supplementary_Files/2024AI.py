#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:49:23 2024

@author: apm
"""

#script--> madule
#yekseri adad
#yekseri class
#yekseri tabe

alpha_silver=130

def ai_calculator(num1,num2,amalgar):
    if amalgar=='jam':
        c=num1+num2
        return c
    elif amalgar=='tafrigh':
        c=num1-num2
        return c
    elif amalgar=='zarb':
        c=num1*num2
        return c
    elif amalgar=='taghsim':
        c=num1/num2
        return c
    else:
        print('eshtebah vared kardid')
        

