t = int(input())
c = int(input())
chores = []
for i in range (c):
    chore = int(input())
    chores.append(chore)

chores.sort()

ostr = 0
for i in range (len(chores)):
    t -= chores[i]
    if t>=0:
        ostr += 1

print (ostr)