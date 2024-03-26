n = int(input())
names = []
bids = []
for i in range (n):
    name = input()
    bid = int(input())
    names.append(name)
    bids.append(bid)

print (names[bids.index(max(bids))])
