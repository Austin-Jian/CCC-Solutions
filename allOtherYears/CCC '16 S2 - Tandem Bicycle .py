t = int(input())
n = int(input())
d = input().split()
p = input().split()

tSpeed = 0
for i in range (len(d)):
    d[i] = int(d[i])
for x in range (len(p)):
    p[x] = int(p[x])
d.sort()
p.sort()

if t == 1:
    for y in range (len(d)):
        if d[y] > p[y]:
            tSpeed += d[y]
        else:
            tSpeed += p[y]
    print (tSpeed)

elif t == 2:
    while len(d) != 0:
        minimum = min(d)
        maximum = max(p)
        if maximum>minimum:
            tSpeed += maximum
        else:
            tSpeed += minimum
        d.remove(minimum)
        p.remove(maximum)
    print (tSpeed)