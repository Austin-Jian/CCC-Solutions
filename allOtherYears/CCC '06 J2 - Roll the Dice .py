m = int(input())
n = int(input())

ways = 0

if n>m:
    m, n = n, m

for i in range (1,n+1):
    if 10-i<=m and 10-i>0:
        ways += 1

if ways == 1:
    print ("There is 1 way to get the sum 10.")
else:
    print (f"There are {ways} ways to get the sum 10.")
