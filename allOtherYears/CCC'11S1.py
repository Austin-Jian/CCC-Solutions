n = int(input())
t = 0
s = 0
for i in range (n):
    istr = input()
    istr = istr.lower()
    t += istr.count('t')
    s += istr.count('s')

if t>s:
    print ("English")
elif s>t:
    print ("French")
else:
    print ("French")