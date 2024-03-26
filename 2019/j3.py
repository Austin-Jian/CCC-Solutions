n = int(input())
ostr1 = []
for i in range (n):
    istr = input()
    firstC = istr[0]
    count = 0
    ostr2 = []
    for x in range (len(istr)):
        if istr[x] == firstC:
            count += 1
        if istr[x] != firstC:
            ostr2.append(count)
            ostr2.append(' ')
            ostr2.append(istr[x-1])
            ostr2.append(' ')
            count = 1
            firstC = istr[x]
        if len(istr)-1 == x:
            ostr2.append(count)
            ostr2.append(' ')
            ostr2.append(istr[x])
            
    ostr1.append(ostr2)

for y in range (len(ostr1)):
    print (*ostr1[y], sep = "")
