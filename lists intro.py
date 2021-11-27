a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print("original value list of a is:", a)
a.append(10)
print("a after being appended 10 is:", a)
a.append(b)
print("a after being appended object b is:", a)
# extending list a using a range of 3
a.extend(range(3))
print("a after being extended by a range of 3", a)
# extending a  using values of b
a.extend(b)
print("a after being extende by value of b is:", a)
c = a + [12, 13, 14] + b
print("the concatenation of a,b and the new list is:", c)
