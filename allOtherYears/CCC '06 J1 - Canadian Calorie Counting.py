tcals = 0
b = int(input())
if b == 1:
    tcals += 461
elif b == 2:
    tcals += 431
elif b == 3:
    tcals += 420

s = int(input())
if s == 1:
    tcals += 100
elif s == 2:
    tcals += 57
elif s == 3:
    tcals += 70

d = int(input())
if d == 1:
    tcals += 130
elif d == 2:
    tcals += 160
elif d == 3:
    tcals += 118


de = int(input())
if de == 1:
    tcals += 167
elif de == 2:
    tcals += 266
elif de == 3:
    tcals += 75

print ("Your total Calorie count is %s." %(tcals))
