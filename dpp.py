#generates page ranges for printing a large book, 4 pages per page, 2 sided

range=int(raw_input("Enter range:"))
seta=""
setb=""
a=""
b=""
i=1
while i<=range:
	if i+1<=range:
		adn="%d,%d"%(i,i+1)
	elif i<=range:
		adn="%d"%(i)
	if i+3<=range:	
		bdn="%d,%d"%(i+2,i+3)
	elif i+2<=range:
		bdn="%d"%(i+2)
	if len(a)!=0 and len(adn)!=0:
		a=a+","
	if len(b)!=0 and len(bdn)!=0:
		b=","+b
	a=a+adn
	b=bdn+b
	adn=""
	bdn=""
	if len(a)>16 or i+4>range:
		seta=seta+a+"\n"
		a=""
	if len(b)>16 or i+4>range:
		setb=b+"\n"+setb
		b=""
	i=i+4
fname="tillpg%d"%(range)
file=open(fname,"w+")
file.write(seta+"\n")
file.write(setb)
file.close()
