n = int(input())
scores = []
for i in range (n):
    score = int(input())
    scores.append(score)

scores.sort()
max = scores[n-1]+1

track = 0
for i in range (len(scores)-1,-1,-1):
    if scores[i]<max:
        track+=1
        max = scores[i]
        if track == 3:
            break
    
print (max, scores.count(max))