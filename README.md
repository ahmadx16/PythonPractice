## PythonPractice
### Inverted Index
This mini project takes in the html files from the Sheep directory which is available at kaggle 

https://www.kaggle.com/uciml/identifying-interesting-web-pages 
and parse them in such a way the 
* Only body text remains, 
* Converts all text to lower case.

The final output of inverted index is on file inverted_index.txt and has following format

**WORD {ALL UNIQUE DOCUMENTS IN WHICH IT OCCURS}**

Sample Tabel:
| Words         | Set of Documents     |
| ------------- |----------------------| 
| Word 1        | {1,23,45,63,33}      |

### How to run 

In InvertedIndex directory execute command
```shell
python3 parse.py
```
