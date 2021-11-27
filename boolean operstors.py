 # if & if not
def orr(a, b):
    if a:
        return a
    else:
        return b


a = 4
b = 32
print(orr(b, a))

x = 3.14
if 2 > x > 3.14:
    print(" x is greater than pi")
else:
    print("x is not greater than pi")