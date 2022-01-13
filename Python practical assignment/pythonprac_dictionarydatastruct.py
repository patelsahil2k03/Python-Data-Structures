#20CE101 CE2 SAHIL PATEL
print("20CE101 SAHIL PATEL")
#A:- Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
print()
print("\n")


#B:- Write a Python script to merge two Python dictionaries.
d1 = {'Actor': 'Tom Holland','Cricketer': 'Virat Kohli','BasketballPlayer': 'Stephen Curry','FootballPlayer': 'Cristiano Ronaldo'}

d2 = {'TennisPlayer ': 'Roger Federer','Stadium ': 'Camp Nou','BasketballPlayer': 'Michael Jordon','Actress': 'Emma Watson'}
# (Defines the d2 dictionary)

d1.update(d2)  # (append the d2 dictionary items into the d1 dictionary.)
print("Merge two dictionaries :")
print(d1)  # (prints the merged dictionary)
print()
print("\n")


#C:- Write a Python program to sum all the items in a dictionary.

dic={ 'x':155, 'y':225, 'z':99, 'p':11 } #(initialisation)

print("Dictionary: ", dic)
print("sum of all the items in the dictionary: ",sum(dic.values()))#(using sum() and values())
print()
print("\n")

#D:- Write a Python script to add a key to a dictionary.
Dict = {"IND": 99, "UK" : 91 , "USA" : 88, "ESP" : 74}
print(Dict)

Dict.update( {'GER' : 108} )
print(Dict)

Dict.update( [('AUS', 101),('EGY',69)] )# (Adding multiple key value pairs)
print(Dict)
print()
print("\n")
#E:- Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
print()
print("\n")

print("SOME BASIC PROBLEMS OF USE OF DICTIONARY DATA STRUCTURE IN PYTHON")