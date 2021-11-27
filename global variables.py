a = 3 #global variable a
b = 12
c = 21
d = 11

def fGtest():
    a = "Samantha" #local variable a
    e = globals()["a"]
    f = globals()["b"]
    g = "jeff"
    print(g)
    print(a)
    global h
    h = "Angayo"

# updating g.v a from 3 to 12 and b from 12 to 9
    globals()["a"] = 12
    globals()["b"] = 9





fGtest()
print(id(a))
print(id(b))
print(a)
print(b)
print(c)
print(d)
print(h)