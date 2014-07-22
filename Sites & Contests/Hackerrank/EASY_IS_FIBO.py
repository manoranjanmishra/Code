#Hackerrank- isFibo
#generate all the numbers of the fibonacci series upto 10**10 & then look them up as needed. If you start with 0,1,1,2,3.. there are only 48 numbers upto 10^10 & 96 upto 10^20.
t=int(raw_input())
a=0
b=1
c=0
fibo_list=(0,1)	# generate & store all the fibonacci numbers in the list.
while((a+b)<=(10**10)):
	c=a+b
	fibo_list=fibo_list+(c,)
	a=b
	b=c
while(t>0):
	n=int(raw_input())
	if(n in fibo_list):
		print "IsFibo"
	else:
		print "IsNotFibo"
	t=t-1
#for 48 numbers a dictionary isn't going to be different from a list, right?
#dictionary version:
t=int(raw_input())
a=0
b=1
c=0
fibo_list={}
fibo_list[0]=0
fibo_list[1]=1	#generate & store all the fibonacci numbers in the dictionary
while((a+b)<=(10**10)):
	c=a+b
	fibo_list[c]=c
	a=b
	b=c
while(t>0):
	n=int(raw_input())
	if(fibo_list.get(n)!=None):	#if the number is a fibonacci number, it will be in the keylist & we'll not get a None result
		print "IsFibo"
	else:
		print "IsNotFibo"
	t=t-1