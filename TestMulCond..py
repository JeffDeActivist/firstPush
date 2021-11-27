# Returns yes
a = 2
b = 3
if a and b > 2:
    print("yes")
else:
    print("no")


# Returns no--which is correct
if a > 2 and b > 2:
    print("yes")
else:
    print("no")

# using a canonical operator
c = 3
if c in (1, 2, 3, 4, 5):
    print("yes")
else:
    print("no")

# this canonical can be used instead of
if c == 1 or c == 2 or c ==3 or c == 4 or c == 5 or c == 6:
    print("yes")
else:
    print("no")

