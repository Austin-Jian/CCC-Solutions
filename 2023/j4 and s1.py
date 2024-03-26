c = int(input())
r1 = input().split()
r2 = input().split()

tape = 0
for i in range (c):
    if r1[i] == '1' and c!=1:
        tape +=3
        if i == 0:
            if r1[i+1] == '1':
                tape -= 1
            if r2[i] == '1' and (i+1)%2!=0:
                tape -= 1
        elif i == c-1:
            if r1[i-1] == '1':
                tape -= 1
            if r2[i] == '1'and (i+1)%2!=0:
                tape -= 1
        else:
            if r1[i+1] == '1':
                tape -= 1
            if r2[i] == '1'and (i+1)%2!=0:
                tape -= 1
            if r1[i-1] == '1':
                tape -= 1
    if r2[i] == '1' and c!=1:
        tape += 3
        if i == 0:
            if r2[i+1] == '1':
                tape -= 1
            if r1[i] == '1'and (i+1)%2!=0:
                tape -= 1
        elif i == c-1:
            if r2[i-1] == '1':
                tape -= 1
            if r1[i] == '1'and (i+1)%2!=0:
                tape -= 1
        else:
            if r2[i+1] == '1':
                tape -= 1
            if r1[i] == '1'and (i+1)%2!=0:
                tape -= 1
            if r2[i-1] == '1':
                tape -= 1
    if c == 1:
        if r1[i] == '1':
            tape += 3
            if r2[i] == '1':
                tape -= 1
        if r2[i] == '1':
            tape += 3
            if r1[i] == '1':
                tape -= 1

print (tape)