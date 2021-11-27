a = 1
b = 2
c = 3


def f_gv():
    d = globals()["a"]
    print(id(d))
    globals()["a"] = 1
    global e
    e = 23
    print("value of e local:", e)


print(id(a))
f_gv()

print("value of a:", a)
print("value of e after being declared global is: ", e)
