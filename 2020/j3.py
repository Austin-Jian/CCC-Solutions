n = int(input())
xList = []
yList = []
for i in range (n):
    xy = input()
    xy = xy.split(",")
    x = xy[0]
    y = xy[1]
    xList.append(int(x))
    yList.append(int(y))

print (f"{min(xList)-1},{min(yList)-1}")
print ((f"{max(xList)+1},{max(yList)+1}"))
