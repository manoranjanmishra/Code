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
    i=1	#factor, runs from 1 till the smallest number in a.sor()
    f=0	#is-divisible flag
    h=0	#highest dividing factor
    while(i<=a[0]):
        for j in a:	#running through all the elements in the list
            if(j%i==0):
                f=0
            if(j%i!=0):
                f=1
                break	#no point checking this number with other numbers in the list a, so try with next i
        if(f==0):
            h=i
        i=i+1
    if(h==1):
        print "YES"
    else:
        print "NO"
    t=t-1		#for the test cases
            