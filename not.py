# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:35:25 2019

@author: PC-ROCK
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:36:38 2019

@author: PC-ROCK
"""

import nltk
import nltk.corpus
with open("food.txt","r",encoding="utf-8-sig") as f:
    data1=f.read() 

with open("music.txt","r",encoding="utf-8-sig") as f:
    data2=f.read() 


 
    

  
from collections import Counter
list_word1=nltk.word_tokenize(data1)    
list_word2=nltk.word_tokenize(data2)

stop = set(nltk.corpus.stopwords.words('english')) 
list_word=[i for i in nltk.word_tokenize(data1) if i not in stop] 
list_word2=[i for i in nltk.word_tokenize(data2) if i not in stop]  



wordcont1=Counter(list_word1)
wordcont2=Counter(list_word2)


with open("result_food.txt","w+",encoding="utf-8") as f:
   f.write(str(dict(wordcont1)))  
   
with open("result_music.txt","w+",encoding="utf-8") as f:
   f.write(str(dict(wordcont2)))    
     
   
allwordcont=Counter(list_word1+list_word2)
with open("resultallword.txt","w+", encoding="utf-8") as f:
      f.write(str(dict(allwordcont)))   
      
list_word_all=list(dict(allwordcont))
list_word_a=list(dict(wordcont1))
list_word_b=list(dict(wordcont2))
inverted_list={}
for i in list_word_all:
    inverted_list[i]=[]
    if i in list_word_a:
        inverted_list[i].append(str(1))
    if i in list_word_b:
        inverted_list[i].append(str(2))   


file=""
for d,index in inverted_list.items():
    file+=d+" : "+str(",".join(index))+"\r\n"
with open("result.txt","w",encoding="utf-8") as f:
    f.write(file)   
    print(file)

name1 = input("input word :")

print(name1)

numlist=[]

for i in list_word_all :
    
    if i in list_word_a and i not in list_word_b:
        if(i==name1):
            numlist.append("ค้นหาเจอ :"+str(1)+" แต่ไม่เจอในไฟล์ :"+str(2))
    
      
    if i in list_word_b:
        if(i==name1):
            numlist.append("เจอในไฟล์ที่"+str(2)+" แต่ไม่เจอในไฟล์ :"+str(1))
      
print(numlist)
