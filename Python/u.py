#Hackerrank - Utopian Tree
def ch(n):
    sh=1
    i=1
    while(i<=n):
		if (i%2!=0):
			sh=sh*2
		else:
			sh=sh+1
		i=i+1
    print sh
t=int(raw_input())
while (t>0):
    ch(int(raw_input()))
    t=t-1