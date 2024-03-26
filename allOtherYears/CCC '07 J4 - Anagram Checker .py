m = input()
n = input()
anagram = True
for i in range (len(m)):
    if m[i]!= ' ':
        if m.count(m[i]) != n.count(m[i]):
            print ("Is not an anagram.")
            anagram = False
            break

if anagram:
    print ("Is an anagram.")