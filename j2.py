p = int(input())
n = int(input())
r = int(input())    
sum = n
day = 0
while p>=sum:
    n *= r
    sum += n
    day += 1

print (day)