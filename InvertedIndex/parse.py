"""
This programs reads files from Sheep directory  (available at kaggle https://www.kaggle.com/uciml/identifying-interesting-web-pages) and parses
 it and creates a Inverted index.
"""

import os
from bs4 import BeautifulSoup
import re

# custom stopword module 
import stopword

word_dic = {}
print(stopword.stopwords)
filenames =  (os.listdir("./Sheep"))
for filename in filenames:
    file1 = open("./Sheep/" +filename,'r')
    soup = BeautifulSoup(file1.read(),'lxml')
    body = soup.find("body")
    # making words case insensitive
    
    body = body.text.lower()
    re_query = '; |, |\*|\n|&|\"|\\s+|`'
    words = re.split(re_query,body)
    print(words)
    
    # makeing a words dictionary 
    
    break



