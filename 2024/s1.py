def check(list):
  x = 0
  if len(list) % 2 == 0:
    check = len(list) // 2
    First = list[check:]
    Second = list[:check]
    for i in range(check):
      if First[i] == Second[i]:
        x += 2
      else:
        x += 0
  return x
n = int(input())
hats = []
for i in range(n):
  x = int(input())
  hats.append(x)
print(check(hats))