A0 = dict(zip(('a','b','c','d','e'),('1','2','3','4','5')))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = sorted (A0[i]for i in A0)
A4 = [[i,i*i] for i in A1]

x = range(5)

list = []
list.append(A0)
list.append(A1)
list.append(A2)
list.append(A3)
list.append(A4)

for i in range(5):
    for j in list[i]:
        print (j)
