# do stuff with tuples

m = (1, 7, 5)

def tplay(tt):
    l1=list()
    for t in range(len(tt)):
       l1.extend((tt[t]+1 ,tt[t]+1 , tt[t]+1))
    return l1

print(tplay(m))
l2 = [m,m,m]
print(l2)
