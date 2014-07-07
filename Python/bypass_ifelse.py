#by passing if else statements. 
#this si something. See how far it goes. 
def cmp(a,b):
	print "Yes"*(a>b)+"No"*(b>a)+"Equal"*(a==b)
	#if you write print "Yes"*(a>b),"No"*(b>a),"Equal"*(a==b) python tends to leave out a space for each comma it encounters. If you replace the commas by plus signs the strings get concatenated and you are left with a clean out put.
try:
	n1=float(raw_input("Enter a number: "))
	n2=float(raw_input("Enter another number: "))
	cmp(n1,n2)
except:
	print "C'mon! Read what I said..Enter a number!"