# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:08:14 2020

@author: gulbarin
Student Name: Gülbarin Maçin
ID: 69163
"""
import random 

#this method create random list which is a original list
def random_list():
    n=random.randint(3,21)
    randomlist = []
    for i in range(n):
        elt = random.randint(1,100)
        randomlist.append(elt)
    print("My list lenght is", n)
    return randomlist
#thanks to this method we can easily sum 3 numbers
def create_sum_of_neighbors_list(list1):
    a=len(list1)
    list2=[]
    for i in range(a):
        if i==0:
            elt=list1[i]+list1[i+1]
            list2.append(elt)
        elif i==a-1:
            elt=list1[i]+list1[i-1]
            list2.append(elt)
        else:
            elt=list1[i-1]+list1[i]+list1[i+1]
            list2.append(elt)
    return list2

#merged 2 list to create 3rd list
def merged_list(list1, list2):
    list3 = []
    len1 = len(list1)
    for i in range(len1):
        list3 += [list1[i]]
        list3 += [list2[i]]
    return list3

#this removeing odd numbers
def del_odd_value(lst):
    for i in lst[:]:
        if i % 2 != 0:
            lst.remove(i)
    return lst

def sum_two_sides(lst):
    new_list=[]
    if len(lst) % 2 == 0:
        for i in range(len(lst)//2):
           elt=lst[i]+lst[len(lst)-i-1]
           new_list.append(elt)
    else:
        n=(len(lst)+2)//2
        m=lst[n-1]
        for i in range(len(lst)//2):
           elt=lst[i]+lst[len(lst)-i-1]
           new_list.append(elt)
        new_list.append(m)
    return new_list

list1= random_list()
print("List1(Original List)")
print(list1)
list2=create_sum_of_neighbors_list(list1)
print("List2 (Sum of neighbors of List1):")
print(list2)
list3= merged_list(list1,list2)
print("List3 (List1 and List2 merged):")
print(list3)
print("List3 with odd numbers removed:")
list3=del_odd_value(list3)
print(list3)
print("List4 (Summing List3 from two sides):")
list4=sum_two_sides(list3)
print(list4)
print("List4 sorted in descending order:")
list4.sort()
print(list4[::-1]) #this print numbers descending order