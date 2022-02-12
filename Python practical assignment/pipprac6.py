#GITHUB REPOSITRY LINK OF SAHIL PATEL 20CE101 :- https://github.com/patelsahil2k03/Python-Data-Structures

#GITHUB ACCOUNT USERNAME :- patelsahil2k03

#GITHUB REPOSITRY NAME :- Python-Data-Structures

#PRACTICAL 6 BY SAHIL PATEL 20CE101

#AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
#Sample Input
#4
#bcdef
#abcdefg
#bcde
#bcdef
#Sample Output
#3
#2 1 1
#Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

import collections; #This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.

N = int(input())
d = collections.OrderedDict() #dict subclass that remembers the order entries were added

for i in range(N):
    word = input()
    if word in d:
        d[word] +=1
    else:
        d[word] = 1

print(len(d));

for k,v in d.items():
    print(v,end = " ");