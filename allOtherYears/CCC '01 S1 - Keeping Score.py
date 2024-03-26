istr = input()
total = 0
value1 = istr.find("D")-istr.find("C")
value2 = istr.find("H")-istr.find("D")
value3 = istr.find("S")-istr.find("H")
value4 = len(istr) - istr.find("h")

print ("Cards Dealt Points")
card = istr[istr.find("C")+1:istr.find("D")]
point = 0
if len(card)==0:
    point+=3
elif len(card)==1:
    point+=2
elif len(card)==2:
    point+=1
point += card.count("A")*4
point += card.count("K")*3
point += card.count("Q")*2
point += card.count("J")
total += point
if value1>0:
    print ("Clubs", " ".join(card), point)
else:
    print ("Clubs", point)


card = istr[istr.find("D")+1:istr.find("H")]
point = 0
if len(card)==0:
    point+=3
elif len(card)==1:
    point+=2
elif len(card)==2:
    point+=1
point += card.count("A")*4
point += card.count("K")*3
point += card.count("Q")*2
point += card.count("J")
total += point
if value1>0:
    print ("Diamonds", " ".join(card), point)
else:
    print ("Diamonds", point)


card = istr[istr.find("H")+1:istr.find("S")]
point = 0
if len(card)==0:
    point+=3
elif len(card)==1:
    point+=2
elif len(card)==2:
    point+=1
point += card.count("A")*4
point += card.count("K")*3
point += card.count("Q")*2
point += card.count("J")
total += point
if value1>0:
    print ("Hearts", " ".join(card), point)
else:
    print ("Hearts", point)


card = istr[istr.find("S")+1:len(istr)]
point = 0
if len(card)==0:
    point+=3
elif len(card)==1:
    point+=2
elif len(card)==2:
    point+=1
point += card.count("A")*4
point += card.count("K")*3
point += card.count("Q")*2
point += card.count("J")
total += point
if value1>0:
    print ("Spades", " ".join(card), point)
else:
    print ("Spades", point)

print ("Total", total)