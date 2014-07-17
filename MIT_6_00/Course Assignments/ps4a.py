#Problem Set 4 - Course Assignment MIT Course 6_00
#Problem-1
def nestEggFixed (salary, save, growthRate, years):
	F=[salary*save*0.01]
	for i in range (1,years):	#since we have already set the value of F[0] we start from the next element till the end.
		value=F[i-1]*(1+0.01*growthRate)+salary*save*0.01
		F.append(value)
	return F
#print nestEggFixed(int(raw_input("Salary: ")),int(raw_input("Save Rate: ")),int(raw_input("Growth Rate: ")),int(raw_input("Years: ")))
#Problem-2
def nestEggVariable(salary, save, growthRates):
	#growthRates is a list of growth rates, and since each value corresponds to a year, it also represents the years worked
	F=[salary*save*0.01]
	for i in range(1,len(growthRates)):
		value=F[i-1]*(1+0.01*float(growthRates[i]))+salary*save*0.01	#When the user inputs growth rates, we'll be reading it in as a string, ans slicing it to form a list. So, it makes sense to convert it into float when we use it.
		F.append(value)
	return F
#print nestEggVariable(int(raw_input("Salary: ")),int(raw_input("Save: ")),raw_input("Growth Rates: ").split(' '))
#Problem-3
def postRetirement(savings, growthRates, expenses):
	F=[(savings*(1+0.01*int(growthRates[0])))-expenses]
	i=1
	while(i<len(growthRates)):
		F.append(F[i-1]*(1+0.01*int(growthRates[i]))-expenses)
		i=i+1
	return F
#print postRetirement(int(raw_input("Savings: ")),raw_input("Growth Rates: ").split(" "),int(raw_input("Expenses: ")))
#Problem-4
def findMaxExpenses(salary, save, prg, arg, epsilon):	#def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon): 
	F_W=nestEggVariable(salary,save,prg)
	#implementing binary-search.
	l=0			#define a low value
	h=F_W[-1]	#define a high value
	guess=(l+h)/2
	c=0			#count the number of iterations
	while True:
		F_R=postRetirement(F_W[-1],arg,guess)		#we want F_R[-1] to be zero. The start of the retirement fund is the amount left at the end of the last working year.
		#print c,F_R[-1],F_W[-1]	#Use this to see the guesses as iterations continue
		if((F_R[-1])>(0-epsilon))&((F_R[-1])<(0+epsilon)):
			print "Number of Iterations: ",c
			print "Optimal Expenses: ",guess
			break
		elif((F_R[-1])<(0-epsilon)):	#too high expenditure, so lower guess
			h=guess
			guess=(l+h)/2
		elif((F_R[-1])>(0+epsilon)):	#too low expenditure, raise guess
			l=guess
			guess=(l+h)/2
		c=c+1
print findMaxExpenses(float(raw_input("Salary: ")),float(raw_input("Savings: ")),raw_input("Pre-Retirement Growth Rates: ").split(" "),raw_input("Post Retirement Growth Rates: ").split(" "),float(raw_input("Epsilon: ")))