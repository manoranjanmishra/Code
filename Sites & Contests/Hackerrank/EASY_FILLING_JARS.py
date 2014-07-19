#Hackerrank: filling jars https://www.hackerrank.com/challenges/filling-jars
i=raw_input().split(" ")
n=int(i[0])
m=int(i[1])
sum=0
while(m>0):
    i=raw_input().split(" ")
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    sum=sum+(b-a+1)*c
    m=m-1
print int(sum/n)