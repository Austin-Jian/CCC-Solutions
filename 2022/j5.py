M = int(input())
N = int(input())
t1 = []
while N > 0:
    xy = input()
    t1.append(tuple(map(int, xy.split(' '))))
    N -= 1

def solve(trees, M):
    ans = 0
    pos = [(0,0)] + trees + [(M, M)]
    for i in range(len(pos)):
        for j in range(len(pos)):
            if i != j:
                mn = min(M - pos[i][0], M - pos[j][1])
                for k in range(len(pos)):
                    if k != i and k != j and \
                       pos[k][0] > pos[i][0] and pos[k][1] > pos[j][1]:
                       if pos[k][0] - pos[i][0] - 1 >= mn or pos[k][1] - pos[j][1] - 1 >= mn:
                           continue

                       mn = max(pos[k][0] - pos[i][0], pos[k][1] - pos[j][1]) - 1
                
                ans = max(mn, ans)
    return ans

t2 = [(e[0], M - e[1] + 1) for e in t1]
t3 = [(M - e[0] + 1, M - e[1] + 1) for e in t1]
t4 = [(M - e[0] + 1, e[1]) for e in t1]

print(max(solve(t1, M), solve(t2, M), solve(t3, M), solve(t4, M)))