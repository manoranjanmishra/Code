#Hacker rank: Game of Rotation: https://www.hackerrank.com/contests/101apr14/challenges/game-of-rotation
#The handicap is that we process the string for numbers each time. This takes more time, than creating an array, and then using it to calculate pmean. though the code is correct, it takes too long to process.
def rotation(N,a):
	max_sum=0
	count=1
	while(count<=N):
		i=0 #for the index of the string
		n=count #for calculating the position of the extracted number.
		b=" "
		sum=0
		while (i<len(a)):#to process the string untill the string ends.
			while(i<len(a)):
				if (a[i]!=" "):
					b=b+a[i]
				else:
					i=i+1
					break
				i=i+1
			b=int(b[1:])#convert b into a number.
			sum=sum+b*n
			b=" "#reset b to a string type
			n=n+1
			if (n>N):
				n=1	#this is so that if n exceeds N, we reset it to 1, so that it goes in a cyclic order.
		if (sum>max_sum):
			max_sum=sum
		count=count+1
	print max_sum
#N=int(raw_input())
#a=raw_input()
rotation(int(raw_input()),raw_input())