def f_while_loop():
    global a
    a = 23
    while a < 60:
        if a == 55:
            break
        print(a)
        a += 1


f_while_loop()
print(a)
