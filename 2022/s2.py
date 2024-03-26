#Creates dictionaries
union_dict = {}
disjoint_dict = {}
union_used = {}
disjoint_used = {}

#User inputs x restrictions
X = int(input())
while X > 0:
    a, b = input().split(' ')
    if a not in union_dict:
        union_dict[a] = []

    if b not in union_dict:
        union_dict[b] = []

    union_dict[a].append(b)
    union_dict[b].append(a)
    X -= 1

#User inputs y restrictions
Y = int(input())
while Y > 0:
    a, b = input().split(' ')
    if a not in disjoint_dict:
        disjoint_dict[a] = []

    if b not in disjoint_dict:
        disjoint_dict[b] = []

    disjoint_dict[a].append(b)
    disjoint_dict[b].append(a)
    Y -= 1

#User inputs teams
G = int(input())

def check(a, b, c):
    res = 0
    if a in union_dict:
        for e in union_dict[a]:
            if e != b and e != c:
                t1, t2 = a, e
                if t1 > t2:
                    t1, t2 = t2, t1
                key = t1 + '+' + t2
                if key not in union_used:
                    union_used[key] = True
                    res += 1

    if a in disjoint_dict:
        for e in disjoint_dict[a]:
            if e == b or e == c:
                t1, t2 = a, e
                if t1 > t2:
                    t1, t2 = t2, t1
                key = t1 + '+' + t2
                if key not in disjoint_used:
                    disjoint_used[key] = True
                    res += 1
    return res

ans = 0
while G > 0:
    G -= 1
    a, b, c = input().split(' ')
    ans += check(a, b, c) + \
           check(a, c, b) + \
           check(b, a, c) + \
           check(b, c, a) + \
           check(c, a, b) + \
           check(c, b, a)
    
print(ans)