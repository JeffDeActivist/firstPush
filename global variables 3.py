a = 1
b = 2
c = 3


def g_var():
    d = globals()["a"]
    e = globals()["b"]
    f = globals()["c"]
    a = 123
# defining location id of variables d,e,f,a
    print("id of a in:", id(d))
    print("id of b in:", id(e))
    print("id of c in:", id(f))
    print("id of lv.a in:", (id(a)))
    print("value of lv.a in:", a)
# function f_fun nested inside fun g_var
    def f_fun():
        print("value of a called inFoutside:", a)

    f_fun()



g_var()
# printing location id of global variables defined at the begining
print("id of a out:", id(a))
print("id of b out:", id(b))
print("id of c out:", id(c))
print("value of a out:", a)



