istr = input()
decimal = 0
big = 0
for i in range (len(istr)-1,-1,-2):
    if istr[i] == "I":
        if 1>=big:
            big = 1
            decimal += int(istr[i-1])
        else:
            decimal -= int(istr[i-1])
            big = 1
    elif istr[i] == "V":
        if 5>=big:
            big = 5
            decimal += int(istr[i-1])*5
        else:
            decimal -= int(istr[i-1])*5
            big = 5
    elif istr[i] == "X":
        if 10>=big:
            big = 10
            decimal += int(istr[i-1])*10
        else:
            decimal -= int(istr[i-1])*10
            big = 10
    elif istr[i] == "L":
        if 50>=big:
            big = 50
            decimal += int(istr[i-1])*50
        else:
            decimal -= int(istr[i-1])*50
            big = 50
    elif istr[i] == "C":
        if 100>=big:
            big = 100
            decimal += int(istr[i-1])*100
        else:
            decimal -= int(istr[i-1])*100
            big = 100
    elif istr[i] == "D":
        if 500>=big:
            big = 500
            decimal += int(istr[i-1])*500
        else:
            decimal -= int(istr[i-1])*500
            big = 500
    elif istr[i] == "M":
        if 1000>=big:
            big = 1000
            decimal += int(istr[i-1])*1000
        else:
            decimal -= int(istr[i-1])*1000
            big = 1000

print (decimal)