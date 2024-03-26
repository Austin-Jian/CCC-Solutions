l = int(input())
msgList = []
for i in range (l):
    numb, char = input().split()
    msgList.append((int(numb)*char))

for i in range (len(msgList)):
    print (msgList[i])