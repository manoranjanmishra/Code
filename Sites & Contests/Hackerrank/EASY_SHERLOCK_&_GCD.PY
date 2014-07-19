#Hackerrank: Sherlock & GCD
t=int(raw_input())
while(t>0):
    n=int(raw_input())
    a=raw_input().split(" ")
    i=0
    while(i<n):
        a[i]=int(a[i])
        i=i+1
    a.sort()
    i=1
    f=0
    h=0
    while(i<=a[0]):
        for j in a:
            if(j%i==0):
                f=0
            if(j%i!=0):
                f=1
                break
        if(f==0):
            h=i
        i=i+1
    if(h==1):
        print "YES"
    else:
        print "NO"
    t=t-1
            