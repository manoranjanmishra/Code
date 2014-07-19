#Hackerrank - Bill Gates & The Angry Children Problem
n=int(raw_input())
k=int(raw_input())
a=[]
while (n>0):
	a.append(int(raw_input()))
	n=n-1
#now we have a list of values. Time to sort it.
a.sort()
#now we have a sorted list. 
max=None
min=None
i=0
while((i+k-1)<len(a)):
	p=a[(i+k-1)]-a[i]
	if(p<min)or(min==None):
		min=p
	if(p>max)or(max==None):
		max=p
	i=i+1
print min