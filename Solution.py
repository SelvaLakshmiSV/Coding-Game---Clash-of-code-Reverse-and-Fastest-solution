a1=[]
a2=[]
n,l=[int(i) for i in input().split()]
for i in range(l):
    v, s = [int(j) for j in input().split()]
    a1.append(v)
    a2.append(s)
c=0
a1=list(set(a1))
a2=list(set(a2))
# for i in a1:
#     if i in a2:
#         c+=1
if a1 == a2:
    print("CLIQUE")
else:
    print("NOTHING TO SEE HERE")
