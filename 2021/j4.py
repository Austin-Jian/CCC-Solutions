istr = input()

l = istr.count("L")
m = istr.count("M")
s = istr.count("S")

ostr = []
if m == 0:
    for i in range (l):
        ostr.append("L")
    for i in range (m):
        ostr.append("M")
    for i in range (s):
        ostr.append("S")

    ostr = ''.join(ostr)
    change = 0
    for i in range (len(istr)):
        if istr[i] != ostr[i]:
            change += 1
    print (int(change/2))
else:
    for i in range (l):
        ostr.append("L")
    for i in range (m):
        ostr.append("M")
    for i in range (s):
        ostr.append("S")

    ostr = ''.join(ostr)
    change = 0
    for i in range (len(istr)):
        if istr[i] != ostr[i]:
            change += 1
    print (change-1)