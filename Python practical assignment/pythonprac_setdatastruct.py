#20CE101 CE2 SAHIL PATEL
print("20CE101 SAHIL PATEL")
#A:- Write a Python program to add member(s) in a set and clear a set.
SET = {'F', 'l', 'a', 's', 'h'}
SET.add('runnnn!')
print("Letters are:", SET)
print("Set before clear:", SET)
print("Set after clear:", SET.clear())
print()
print("\n")


#B:- Write a Python program to remove an item from a set if it is present in the set.

BigBangTheory = {'Sheldon Cooper', 'Howard Wolowitz', 'Rajesh Koothrappali', 'Leonard Hofstadter'}
print(BigBangTheory)
# remove Sheldon Cooper from the set
BigBangTheory.remove('Sheldon Cooper')
print(BigBangTheory)
#You can use the "set discard()" method if you do not want error in Deleting Element That Doesn't Exist in the set.
print()
print("\n")


#C:- Write a Python program to create an intersection, Union, difference of sets.
# (sets are defined)
A = {0, 2, 4, 6, 8, 10};
B = {1, 2, 3, 4, 5, 6};

# (union in 2 ways)
print("Union :", A | B)
print("Union of A and B:", A.union(B))


# (intersection in two ways)
print("Intersection :", A & B)
print("Intersection of A and B:", A.intersection(B))

# (difference in 2 ways)
print("Difference :", A - B)
print("Difference of A and B:", A.difference(B))

# (symmetric difference in two ways)
print("Symmetric difference :", A ^ B)
print("Symmetric Difference of A and B:", A.symmetric_difference(B))
print()
print("\n")


#D:- Write a Python program to find maximum and the minimum value in a set.
#Create a set
setmarks = {89, 69, 99, 76, 59, 62}
print("Original set of marks:")
print(setmarks)
print(type(setmarks))
print("\nMaximum value of the said set(marks scored):")
print(max(setmarks))
print("\nMinimum value of the said set(marks scored):")
print(min(setmarks))
print()
print("\n")


#E:- Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
list1 = [1, 2, "ABC", 3.4, "ABC"]
tuple1 = (12, 20, "ABC", 3.4, "ABC", 3.4, "ABC", 3.4)
dictionary1 = {'u': "ABC",'v': "ABC", 'w': "ohhh", 'x': 3.4, 'y': 3.4, 'z': 4.8,'a': "ABC", 'b': "ohhh", 'c': 3.4, 'e': 3.4, 'f': 4.9,'g': "ABC", 'h': "ohhh", 'i': 3.4, 'j': 3.4, 'k': 4.7}
dictionary1_list = dictionary1.values()
print("printing dictionary=" ,dictionary1)
print("Type of variable dictionary1 is: ", type(dictionary1_list))

dictionary1_list = list(dictionary1_list)

print("Printing the entire list containing all values: ")
print(dictionary1_list)
sah1 = set(list1)
sah2 = set(tuple1)
sah3 = set(dictionary1_list)

print("List =", list1)
print("Tuple =", tuple1)
print("Dictionary values =", dictionary1_list)

set1 = sah1.intersection(sah2)
result_set1 = set1.intersection(sah3)
final_list = list(result_set1)
print(dictionary1_list)

print()
print("Common members of list, tuple and dictionary:", final_list)

count1 = list1.count("ABC")
count2 = list1.count(3.4)
print("Occurences:", count1)
print("Occurences:", count2)

count3 = tuple1.count("ABC")
count4 = tuple1.count(3.4)
print("Occurences:", count3)
print("Occurences:", count4)

count5 = dictionary1_list.count("ABC")
count6 = dictionary1_list.count(3.4)
print("Occurences:", count5)
print("Occurences:", count6)

print()
print("\n")

print("SOME BASIC PROBLEMS OF USE OF SET DATA STRUCTURE IN PYTHON")