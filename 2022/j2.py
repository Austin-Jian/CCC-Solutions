stars = []
starPlayer = 0
goldTeam = True
N = int(input())
for i in range (N):
    P = int(input())
    F = int(input())
    star = P*5-F*3
    stars.append(star)

for i in range (len(stars)):
    if stars[i]<=40:
        goldTeam = False
    if stars[i]>40:
        starPlayer += 1

if goldTeam:
    print (f"{starPlayer}+")
else:
    print (starPlayer)
