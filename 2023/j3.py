n = int(input())
aList = []
for i in range (n):
    a = input()
    aList.append(a)

largest = 0

d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0

for i in aList:
    if i[0] == "Y":
        d1 += 1
    if i[1] == "Y":
        d2 += 1
    if i[2] == "Y":
        d3 += 1
    if i[3] == "Y":
        d4 += 1
    if i[4] == "Y":
        d5 += 1

day = []
if d1>=d2 and d1>=d3 and d1>=d4 and d1>= d5:
    day.append("1")
if d2>=d1 and d2>=d3 and d2>=d4 and d2>= d5:
    day.append("2")
if d3>=d1 and d3>=d2 and d3>=d4 and d3>= d5:
    day.append("3")
if d4>=d1 and d4>=d2 and d4>=d3 and d4>= d5:
    day.append("4")
if d5>=d1 and d5>=d2 and d5>=d3 and d5>= d4:
    day.append("5")

print (','.join(day))
