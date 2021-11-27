def counter():
    num = 0
    def incrementer ():
            nonlocal num
            num += 1
            return num
    return incrementer()
print(counter())