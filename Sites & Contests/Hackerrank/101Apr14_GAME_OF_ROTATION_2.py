#Hackerrank: Game of Rotation (submission 2)
#rewrote code using find. Time Out, but score improved to 11.25
n=int(raw_input())
a=raw_input()
l=len(a)
c=1
max_pmean=None
while (c<=n):
    sum=0
    i=0
    m=c
    while(i<l):
        if(i==0):
            i1=-1
        else:
            i1=a.find(" ",i)
        i2=a.find(" ",i1+1)
        if(i2==-1):
            num=float(a[(i1+1):])
            i=l
        if(i2!=-1):
            num=float(a[(i1+1):i2])
            i=i2
        sum=sum+num*m
        m=m+1
        if(m>n):
            m=1
    if(sum>max_pmean)or(max_pmean==None):
        max_pmean=sum
    c=c+1
print int(max_pmean)