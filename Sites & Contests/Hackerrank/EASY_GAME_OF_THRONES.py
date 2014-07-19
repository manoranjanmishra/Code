#Hackerrank: Game of Thrones - 1
a=raw_input()
p={}
for i in a:
    if (i in p):
        p[i]=p[i]+1
    else:
        p[i]=1
l=len(a)
c=0
c_v=p.values()
for i in c_v:
    if(i%2!=0):
        c=c+1
if(((l%2==0)&(c==0))or((l%2==1)&(c==1))):
    print "YES"
else:
    print "NO"
    