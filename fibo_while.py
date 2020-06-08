def fibo(n):
    t1=0
    t2=1
    lst=[0,1]
    print("fibonacci series:")
    nex = t1 + t2
    while nex <= n:
        lst.append(nex)
        t1 = t2
        t2 = nex
        nex = t1 + t2
    print(lst)
fibo(9)