# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:15:58 2021

@author: dell
"""

#program to allow  a person enter a club based on the age

age = input('How old are you?')
if age:
    age = int(age)
    if age >= 21:
        print("You are eligible to enter. You are allowed to drink")
    elif age >= 18:
        print("You can enter, but you need a wristband")
    else:
        print("You can't come in. You are not of age")