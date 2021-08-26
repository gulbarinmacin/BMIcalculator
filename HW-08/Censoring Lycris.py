# -*- coding: utf-8 -*-
"""
Homework#8 Strings: Censoring lyrics
Gülbarin Maçin /69163
1.12.2020
"""


# DO NOT CHANGE BELOW THIS LINE!!!
text = "We're no strangers to love&You know the rules and so do I@A full\
        commitment's what I'm thinking of@You wouldn't get this from any\
          other guy%I just wanna tell you how I'm feeling&Gotta make you\
       understand$Never gonna give you up$Never gonna let you down@Never\
    gonna run around and desert you%Never gonna make you cry&Never gonna\
        say goodbye%Never gonna tell a lie and hurt you@We've known each\
    other for so long%Your heart's been aching but you're too shy to say\
        it$Inside we both know what's been going on$We know the game and\
     we're gonna play it@And if you ask me how I'm feeling&Don't tell me\
     you're too blind to see$Never gonna give you up%Never gonna let you\
    down&Never gonna run around and desert you$Never gonna make you cry%\
     Never gonna say goodbye@Never gonna tell a lie and hurt you$No, I'm\
       never gonna give you up%No, I'm never gonna let you down&No, I'll\
   never run around and hurt you$Never, ever desert you&We've known each\
     other for so long@Your heart's been aching but$Never gonna give you\
       up%Never gonna let you down@Never gonna run around and desert you\
    $Never gonna make you cry$Never gonna say goodbye@Never gonna tell a\
    lie and hurt you%No, I'm never gonna give you up%No, I'm never gonna\
    let you down@No, I'll never run around and hurt you&I'll never, ever\
                                                              desert you"
        
# DO NOT CHANGE ABOVE THIS LINE!!!
#This is for deleting symbols and print with lines
def replace_symbols(s,c):
    symbols= '&@%$'
    for ch in symbols:
        s= s.replace(ch,c)
    return s
#This is for counting substring in a given text
def count_word(s,ss):
    s= s.lower()
    ss= ss.lower()
    k= s.find(ss,0)
    count= 0
    while k>=0:
        count += 1
        k= s.find(ss,k+1)
    return count 
#This is for censor the given words
def censoring_word(word):
    for i in range(1, len(word)):
        word=word.replace(word[i], '*')
        new_word=word
    return new_word

#I applied all method below this line
censoring_text='' #I decleared this to print censoring lycris
new_text=replace_symbols(text,'\n') #We remove the all symbols and thanks to \n we can print line by line
while '  ' in new_text: #this while remove multiple space and replace single space
    new_text = new_text.replace('  ', ' ')
#printing lycris 
print("LYCRIS")
print(new_text)
#I am asking censor word to user and count the occurences of word
word=input("Enter the word you want to censor: ")
n=count_word(new_text,word)
print(n, " incident(s) found!")
#after asking word, I censor it
censoring_text=new_text.replace(word, censoring_word(word))
#asking user wants more word or not ?
question=input("Do you want to censor more words? ")
if question[0]!="y" or question[0]!="Y":
    print("Please give a proper answer")
    question=input("Do you want to censor more words? ")
while question[0]=="y" or question[0]=="Y":
    word=input("Enter the word you want to censor: ")
    n=count_word(new_text,word)
    print(n, " incident(s) found!")
    censoring_text=censoring_text.replace(word, censoring_word(word))
    question=input("Do you want to censor more words? ")


if question[0]=='N' or question[0]=="n" :
    #if user give N or n I printed censored lycris
    print(" ")
    print("CENSORED LYCRIS")
    print(censoring_text)


















