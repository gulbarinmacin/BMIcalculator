# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:16:41 2020

@author: gulbarin

Student Name: Gülbarin Maçin
Id:69163
"""

first_value = 1 # define outside the loop what is first value of the longest sequence 
largest_sequence = 1 # define outside the loop what is the longest sequence 
for i in range (1,100000): 
    number=i
    lenght=1
    while number!=1:
        if number%2==0:
            next=number/2
        else:
            next=3*number+1
        lenght+=1
        number=next
        if lenght>largest_sequence:
            largest_sequence=lenght
            first_value=i

print('The longest sequence has' ,largest_sequence, 'elements.')
print('It starts with the number:', first_value)
    

