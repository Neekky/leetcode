L1 = ['Hello', 'World', 18, 'Apple', None]
n=0
m=[]
for x in L1:
   a=L1[n]
   n = n + 1
   if isinstance(a,str):
        m.append(x)
print(m)