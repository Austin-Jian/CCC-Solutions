cases = []
t = int(input())


for i in range (t):
    case = []
    n = int(input())
    for x in range (n):
        candy = int(input())
        case.append(candy)
    cases.append(case)

for y in range (t):
    cList = cases[y]
    need = 1
    branch = []
    while True:
        if len(cList) > 0:
            if cList[-1] == need:
                need += 1
                cList.pop()
            elif len(branch)>0:
                if branch[-1] == need:
                    need += 1
                    branch.pop()
                else:
                    branch.append(cList.pop())
            else:
                branch.append(cList.pop())
        elif len(branch)>0:
            if branch[-1] == need:
                need+=1 
                branch.pop()
            else:
                print ("N")
                break
        else:
            print ("Y")
            break