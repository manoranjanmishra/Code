#program for ex2.4 number 2
#to calculate the wholesale cost  for 60 copies
print " This program will calculate the wholesale cost of 60 copies"
#one could include a lot of variables here but we will stick with the question for now
num_books=60
cover_price=24.95 #you cant enter the cover price with the dollar sign here. that is because the python interpreter doesnt accept the $ sign as a number
discount=40 #same case here too, you cant enter the % sign because it is not accepted as a number
cost=(num_books)*(cover_price)*(1-0.4)+3+0.75*(num_books-1) #this is to put in the formula that the question provides.
print "The total wholesale cost for",num_books,"copies is $",cost," at $",cover_price," a book, 75 cents per extra copy shipped"