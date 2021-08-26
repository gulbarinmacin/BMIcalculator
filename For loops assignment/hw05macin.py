# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:32:02 2020

@author: gulbarin

Student Name / ID: Gülbarin Maçin /69163

"""
sum =0 #we should compute all distance so I initilazed sum
month_days=0  # every month has a different day such as 30, 31 so 
              # I created this variable to calculate easily
 
for i in range (1,13): #they are 12 months. In this for 13 is not included so for is runnning 12 times.
    print ('MONTH', i) # to write month number I used i 
    distance=0 # this is for calculate every month distance
    half=0 #it is for half marathon
    #first I findiing month days for each month
    if i==2:
        month_days=29
    elif i==4 or i ==6 or i==9 or i==11:
        month_days=30
    else: 
        month_days=31
    active_days=int((month_days-1)/3)+1
    #every month has a same formula so this variable will be use for calculate active days
    #after finding month days I should find distance
    if i==3 or i==4 or i==5:
    #quarantinaa days
        distance=0
        active_days=0
    else:
        for k in range (1,month_days+1, 3):
            b=k/2+i #k/2 means 1/2 or 7/2 etc.
            distance+=b
            if b >21.1: #this is for half marathon
                half +=1
        sum=sum+distance
    print ('You were active' , active_days, 'of' ,month_days,'days.')
    print ('You have run' , distance ,'.')
    if half >0:
        print('You have run at least a half marathon' ,half,' time(s)')
    print(' ') 
    
print('You have run' ,sum, 'km in 2020.') #We have print sum out of for 