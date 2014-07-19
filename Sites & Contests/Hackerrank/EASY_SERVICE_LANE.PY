#Hackerrank - Service Lane Problem
#Between the given indices print the smallest value in the list.
a=raw_input().split(" ")
n=int(a[0])
t=int(a[1])
width=raw_input().split(" ")
i=0
while(i<len(width)):
    width[i]=int(width[i])
    i=i+1
while(t>0):
    a=raw_input().split(" ")
    p=int(a[0])
    q=int(a[1])
    type=None
    while(p<=q):
        if(width[p]<type)or(type==None):
            type=width[p]
        p=p+1
    print type
    t=t-1