R = int(input())
S = int(input())

cupCakes = 0
if  type(R)==int and R>0:
  cupCakes += R*8

if type(S) == int and S>0:
  cupCakes += S*3

print (cupCakes-28)
