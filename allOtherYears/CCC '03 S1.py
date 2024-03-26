ostr = []
start = 1
while True:
    roll = int(input())
    win = False
    if roll == 0:
        break
    else:
        if start+roll <= 100:
            start+=roll
        if start == 9:
            start = 34
        elif start == 54:
            start = 19
        elif start == 40:
            start = 64
        elif start == 90:
            start = 48
        elif start == 67:
            start = 86
        elif start == 99:
            start = 77
    if start == 100:
        ostr.append(f"You are now on square {start}")
        win = True
        break
    ostr.append(f"You are now on square {start}")

for i in range (len(ostr)):
    print(ostr[i])

if not win:
    print ("You Quit!")
else:
    print ("You Win!")