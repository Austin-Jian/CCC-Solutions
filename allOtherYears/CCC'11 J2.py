h = int(input())
t = int(input())
g = True
for i in range (1,t+1):
    a = -6*i**4+h*i**3+2*i**2+i
    if a<=0:
        print ("The balloon first touches ground at hour:")
        print (i)
        g = False
        break

if g:
    print ("The balloon does not touch ground in the given time.")
