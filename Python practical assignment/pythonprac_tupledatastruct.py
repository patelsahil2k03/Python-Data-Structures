#20CE101 CE2 SAHIL PATEL
print("20CE101 SAHIL PATEL")
#A:- Write a Python program to create a tuple with different data types.
# Different types of tuples

# (Empty tuple)
my_tuple = ()
print(my_tuple)

# (Tuple having integers)
my_tuple = (1, 2, 3)
print(my_tuple)

# (tuple with mixed datatypes)
my_tuple = (1, "Hello my name is Sahil", 3.4)
print(my_tuple)

# (nested tuple)
my_tuple = ("FOOTBALLISLIFE", [8, 4, 6], (1, 2, 3))
print(my_tuple)
print()
print("\n")


#B:- Write a Python program to create a tuple with numbers and print one item.

#(Create a tuple with numbers)
tuplex1 = 101, 102, 103, 555, 122
print(tuplex1)
print(tuplex1[2])
#(Create a tuple of one item)
tuplex2 = 619,
print(tuplex2)
print()
print("\n")


#C:- Write a Python program to add an item in a tuple.
intTuple = (10, 20, 30, 40, 50)
print("Tuple Items = ", intTuple)

intTuple = intTuple + (70,)
print("Tuple Items = ", intTuple)

intTuple = intTuple + (80, 90)
print("Tuple Items = ", intTuple)

intTuple = intTuple[2:5] + (11, 22, 33, 44) + intTuple[7:]
print("Tuple Items = ", intTuple)
print()
print("\n")


#D:- Write a Python program to convert a tuple to a string.
tup = ('T', 'u', 'p', 'l', 'e', ' ', 'D', 'a', 't', 'a', 'S', 't', 'r', 'u', 'c', 't' 'u', 'r', 'e', 's')
str =  ''.join(tup)
print(str)
print()
print("\n")


#E:- Write a Python program to find the length of a tuple.
tuple1, tuple2 = (123, 'xyz', 'sahil'), (456, 'abc', 'h', 'e', 'l', 'l', 'o')
print("First tuple length : ", len(tuple1))
print("Second tuple length : ", len(tuple2))
print()
print("\n")

print("SOME BASIC PROBLEMS OF USE OF TUPLE DATA STRUCTURE IN PYTHON")