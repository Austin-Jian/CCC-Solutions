n = int(input())
istr1 = input().split()
istr2 = input().split()

good = True
for i in range (len(istr1)):
    if istr2.index(istr1[i]) != istr1.index(istr2[i]):
        good = False
        break
    if istr2[i] == istr1[i]:
        good = False
        break

if good:
    print ("good")
else:
    print ("bad")