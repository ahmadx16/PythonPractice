"""
This programs reads files from Sheep directory 
(available at kaggle https://www.kaggle.com/uciml/identifying-interesting-web-pages) and parses
 it and creates a Inverted index.
"""

import os
from bs4 import BeautifulSoup
import re

# custom stopword module 
import stopword

# Word_dic will have unique words and the documents in which it occurs
word_dic = {}

filenames =  (os.listdir("./Sheep"))
i=1
for filename in filenames:
    print(i)
    file1 = open("./Sheep/" +filename,'r',errors='ignore')
    
    soup = BeautifulSoup(file1.read().encode("UTF-8"),'lxml')
    body = soup.find("body")
    # making words case insensitive
    if body is None:
        continue
    body = body.text
    body = body.lower()
    re_query = '; |, |\*|\n|&|\"|\\s+|`'
    words = re.split(re_query,body)

    # saving non stopwords(common) into dictionary
    for word in words:
        if word in stopword.stopwords or word=='':
            continue
        if word not in word_dic:
            word_dic[word] = {i}
        elif word in word_dic:
            if i in word_dic[word]:
                continue
            else:
                word_dic[word].add(i)
    
    i+=1


# Word_dic have unique words and the documents in which it occurs

print(word_dic)

# Output file 
wfile = open("inverted_index.txt",'w')
for k,v in word_dic.items():
    wfile.write(k)
    wfile.write(str(v))
    wfile.write("\n")
wfile.close()



    # makeing a words dictionary 
    
    



