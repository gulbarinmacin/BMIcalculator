# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:25:31 2021

@author: gulbarin

Student Name: Gülbarin Maçin
Id: 69163

"""

import matplotlib.pyplot as plt #this is for dam level by months
import matplotlib.pyplot as plt2 #this is for dam level yearly min and max
import csv
#I created 2 method for 2 plot method to read easily
def dam_level_by_monthly(dict_of_file,firstyear,secondyear):
    #this method take an dict and process according to this dict values and keys
    #I used lists for plot
    percentagelist = [] 
    months=[]
    #in thşs for I get only 2019 and 2020 dam levels form my dict named dam_level
    for k, v in dict_of_file.items():
        if k >= firstyear and k <= secondyear: 
            for k1, v1 in v.items():
                months.append(k1)
                percentagelist.append(v1)

    plt.plot(months[1::],percentagelist[1::],'-m') #january is not included
    plt.grid()       
    plt.xlabel('Month')
    plt.ylabel('Level Percentage (%)')
    plt.title('Istanbul Dam Level by Months - 1/2019 to 12/2020')
    ticks2 = list(range(0,120,20)) #arrange the y axis 0, 120 increasing by 20
    plt.xticks(rotation=90)
    plt.yticks(ticks2)
    plt.show()

def dam_level_min_max(dict_of_file):
    years= []
    min_values= []
    max_values= []
   
#this is a nested dict for max and min values in this this key is year 
#and nested dict there are min values and max values
    my_dict = {} 
    for key, val in dict_of_file.items(): 
        max_val = 0
        min_val = 1000
        for ele in val.values(): 
            if ele > max_val: 
                max_val = ele 
            if ele < min_val:
                min_val=ele
        my_dict[key] = { "Max": max_val, "Min" :min_val }

    for key, val in my_dict.items():
        years.append(key)
        min_values.append(my_dict[key]["Min"])
        max_values.append(my_dict[key]["Max"])


     
    plt2.xlabel('Year')
    plt2.ylabel('Level Percentage (%)')
    plt2.title('Istanbul Dam Level Yearly min/max')
    plt2.bar(years, max_values, color="blue")
    plt2.bar(years, min_values, color="red")
    min_chart = min(years)
    max_chart = max(years)
    ticks = list(range(min_chart,max_chart+1)) #to see all year in chart
    plt2.xticks(ticks,rotation='vertical')

#firstly, I created a dictionary from csv file to created list of variables
dam_level = {}

with open('Istanbul_Water.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        year = int(line[0])
        month = int(line[1])
        percentage = float(line[2])
        if year in dam_level:
            dam_level[year][str(month)+"/"+str(year)] = percentage
            #for converting formatting like 1/2019 I should convert month and year int to str
        else:
            dam_level[year] = {str(month)+"/"+str(year): percentage}
#I want to only access to percentage of 2019 and 2020
dam_level_by_monthly(dam_level,2019,2020)
dam_level_min_max(dam_level)