t, n = map(int,input().split())
ostr = []
for i in range (t):
    istr = input()
    check = []
    checked = []
    for x in range (len(istr)):
        if istr[x] not in checked:
            checked.append(istr[x])
            check.append((istr[x],istr.count(istr[x])))
    weights = dict(check)
    previous = False 
    final = True
    for l in range (len(istr)):
        if l == 0:
            if weights.get(istr[l])==1:
                previous = True
        else:
            weight = weights.get(istr[l])
            if weight > 1:
                if previous is False:
                    final = False
                    break
                else:
                    previous = False
            elif weight == 1:
                if previous is True:
                    final = False
                    break
                else:
                    previous = True
    if final:
        ostr.append('T')
    else:
        ostr.append('F')

for a in ostr:
    print (a)