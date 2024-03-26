t = input()
s = input()
cpos = []
s2 = s
if len(s)>=3:
    for i in range (len(s)):
        a = s2[0]
        b = s2[-1]
        pos = s2[1:-1]+b+a
        s2 = pos
        cpos.append(pos)
    p = "no"
    for x in range (len(cpos)):
        if cpos[x] in t:
            p = 'yes'

    print (p)

elif len(s) == 1:
    if s in t:
        print ('yes')
    else:
        print ('no')

elif len(s) == 2:
    if s in t:
        print ('yes')
    elif (s[1] + s[0]) in t:
        print ('yes')
    else: 
        print ('no')