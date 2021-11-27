# intersection
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6}
c = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
print(c)

# union
d = {12, 14, 56, 46}
e = {14, 34, 55}
f = {12, 14, 56, 46}.union({14, 34, 55})
print(f)
# difference
g = {12, 14, 56, 46}
h = {14, 34, 55}
i = {12, 14, 56, 46}.difference({14, 34, 55})
print(i)

# symmetric_difference
j = {12, 14, 56, 46}
k = {14, 34, 55}
l = {12, 14, 56, 46}.symmetric_difference({14, 34, 55})
print(l)

# superset check
m = {1, 2}
n = {2, 1}
o = {1, 2}.issuperset({2, 1})
print(o)
print(m.union(n))

# single sets
s = {1, 2, 3, 4, 6}
s.update({7, 9})
print(s)

# fetching unique elememnts in a list
list1 = [1, 2, 3, 4, 4, 5, 1, 4, 7]
set1 = set(list1)
print("the following is a set of unique elements", set1)
list2 = list(set1)
print(list2)
# to check for existence
print(99 in  list1)
print(len(list1))
print(list1[2])
# unhashable set
q = {{1, 2}, {3, 4}}
print(q)
p = {frozenset({1, 2}), frozenset({2, 4})}
print(p)
