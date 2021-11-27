from array import *

my_array = array('i', [1, 2, 3, 4, 5, 6])
for (i) in my_array:
    # to print all the values in an array
    print(i)
# printing a specific value of an array
print(my_array[2])
# adding a new value to the list of arrays
my_array.append(7)
for (i) in my_array:
    print(i)
# formula 2 for inserting arrays
my_array.insert(11, 11, )
for (i) in my_array:
    print(i)
# to extend an array
emy_array = array('i', [12, 13, 14, 15])
my_array.extend(emy_array)
for (i) in my_array:
    print(i)
# adding a list into an array
my_array2 = [16, 17, 18, 19, 20]
my_array.fromlist(my_array2)
for i in my_array:
    print(i)
# removing an array element
my_array.remove(16)
for (i) in my_array:
    print(i)
# removing last array element using pop()
my_array.pop()
for (i) in my_array:
    print(i)
#  Fetch any element through its index using index()
print(my_array.index(1))
# reversing an array
my_array.reverse()
for (i) in my_array:
    print(i)
# Get array buffer information through buffer_info() method
my_array.buffer_info()
print(my_array.buffer_info())
# : Check for number of occurrences of an element using count() method
my_array.count(4)
print(my_array.count(4))
# converting an array to a string
my_array3 = array("b", ['j', 'e', 'f', 'f'])
my_array3.tostring()
print(my_array3.tostring())
# converting array elements to a list using tolist()
my_array.tolist()
print(my_array.tolist())
