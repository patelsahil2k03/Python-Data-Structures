#GITHUB REPOSITRY LINK OF SAHIL PATEL 20CE101 :- https://github.com/patelsahil2k03/Python-Data-Structures

#GITHUB ACCOUNT USERNAME :- patelsahil2k03

#GITHUB REPOSITRY NAME :- Python-Data-Structures

#PRACTICAL 7 BY SAHIL PATEL 20CE101

#AIM:- Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome.
#Input:
#6
#gaga
#abcde
#rotor
#xyzxy
#abbaab
#ababc
#Output:
#YES
#NO
#YES
#YES
#NO
#NO
for _ in range(int(input())):
    s=input()
    a1={}
    a2={}
    x=len(s)
    start=0
    end=x-1
    while start<end:
        y=s[start]
        m=s[end]
        if y in a1:
            a1[y]=a1[y]+1
        else:
            a1[y]=1
        if m in a2:
            a2[m]=a2[m]+1
        else:
            a2[m]=1
        start=start+1
        end=end-1
    if a1==a2:
        print('YES')
    else:
        print('NO')