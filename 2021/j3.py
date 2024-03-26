ostr = []
inst = ''
while True:
    code = input()
    if code == "99999":
        break
    s = int(code[0])+int(code[1])
    if s%2 == 0 and s!=0:
        m = "right " + code[2:]
        ostr.append(m)
        inst = 'right '
    elif s%2 != 0:
        m = "left " + code[2:]
        ostr.append(m)
        inst = 'left '
    elif s == 0:
        m = inst + code[2:]
        ostr.append(m)

    


for i in range (len(ostr)):
    print (ostr[i])
