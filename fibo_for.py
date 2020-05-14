def fibo(n):
    t1=0
    t2=1
    lst=[0,1]
    print("fibonacci series:")
    for i in range(2,n) :
        nex = t1 + t2
        lst.append(nex)
        t1 = t2
        t2 = nex

    print(lst)
fibo(9)