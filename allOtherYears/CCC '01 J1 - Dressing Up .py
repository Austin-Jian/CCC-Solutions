h = int(input())
stars = 1
for i in range ((h-1)//2):
    print ("*"*stars+" "*((h-stars)*2) + "*"*stars)
    stars += 2
print ("*"*(2*h))
stars-=2
for i in range (((h-1)//2)):
    if stars != 0:
        print ("*"*stars+" "*((h-stars)*2) + "*"*stars)
        stars-=2 
    if stars == 0:
        print ("*"*stars+" "*((h-stars)*2) + "*"*stars, end ='')
