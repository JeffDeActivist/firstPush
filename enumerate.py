# creating an index
for index, item in enumerate(["Math", "Eng", "Kisw", "Bio", "Geog", "Business", "Chem", "Phyc"]):
    print(index, 'for', item)

# iterating over a list
x = map(lambda e: e.upper(), ['one', 'two', 'three'])
print(list(x))
print(x)
