import numpy as np   
def solve():
    while max(d[-1][:-1]) > 0:
        jnum = np.argmax(d[-1][:-1]) #转入下标
        inum = np.argmin(d[:-1,-1]/d[:-1,jnum])  #转出下标
        s[inum] = jnum #更新基变量
        d[inum]/=d[inum][jnum]
        for i in range(bn):
            if i != inum:
                d[i] -= d[i][jnum] * d[inum]
            
def printSol():
    for i in range(cn - 1):
        print("x%d=%.2f" % (i,d[s.index(i)][-1] if i in s else 0))
    print("objective is %.2f"%(-d[-1][-1]))

d = np.loadtxt("data.txt", dtype=np.float)
(bn,cn) = d.shape
s = list(range(cn-bn,cn-1)) #基变量列表
solve()
printSol()
