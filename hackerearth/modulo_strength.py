n,k =  list(map(int,input().split(" ")))
a =  list(map(int,input().split(" ")))
d = {}
for i in range(0,len(a)):
    m = a[i]%k 
    if m not in d:
        d[m] = 1
    else:
        d[m] += 1
s = 0
for k,v in d.items():
    s = s + v*(v-1)
 
print(s)