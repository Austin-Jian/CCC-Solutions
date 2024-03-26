x = int(input())
m = int(input())
n = 1
while True:
    total = x*n
    if total%m == 1:
        print (n)
        break
    if n>= m:
        print ("No such integer exists.")
        break
    n+=1