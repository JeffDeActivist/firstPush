a = 3
b = 4
print(b and a)
print(b or a)


# Lazy expression
def f_lazy():
    print("This is a lazy expression illustration")


0 and f_lazy() # is not executed  bt if or replaces and it's executed