n = int(input())

ways = 0
pairs = set()

for i in range(n // 4 + 1):
    remaining = n - i * 4
    if remaining % 5 == 0:
        ways += 1
        pairs.add((i, remaining // 5))

for i in range(n // 5 + 1):
    remaining = n - i * 5
    if remaining % 4 == 0 and (remaining // 4, i) not in pairs:
        ways += 1

print(ways)
