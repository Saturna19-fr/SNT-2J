def Ex1N1():
    L = [10, 14, 15, 18, 20]
    r=L[0]+L[3]
    print(r)
    return r

def Ex1N2():
    L = [0,0,0,0]
    for i in range(0,4):
        L[i]=i
    print(L)
    return L

def Ex1N3():
    L = [0,0,0,0]
    for i in range(0, 4):
        L[i] = 2*i
    print(L[3])

print('-- EX1 | N1 --')
Ex1N1()
print('-- EX1 | N2 --')
Ex1N2()
print('-- EX1 | N3 --')
Ex1N3()