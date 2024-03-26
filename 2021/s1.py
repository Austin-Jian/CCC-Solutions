n = int(input())
h = input().split()
w = input().split()

for i in range (len(h)):
    h[i] = int(h[i])
for i in range (len(w)):
    w[i] = int(w[i])

area = 0
for x in range (n):
    if h[x]>h[x+1]:
        area += w[x]*h[x]-(abs(h[x]-h[x+1])*w[x])/2
    else:
        area += w[x]*h[x]+(abs(h[x]-h[x+1])*w[x])/2

print(area)
