
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

def andword(word1):
    numlist=[]
    if word1 in inverted_list:
        v1=inverted_list[word1]
       
        for i in v1:
                numlist.append(i)
    return "อยู่ในเอกสาร : "+str(numlist)
name1 = input("input word :")

print(andword(name1))