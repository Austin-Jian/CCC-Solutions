#User inputs the tuning instruction
istr = input()

#Defines variables bk and fd with values of 0
bk, fd = 0, 0

#Creates while loop with condition of fd being less than the instruction
while fd < len(istr):
    #Checks if the letter is '+'... if it is, then replace it with tighten
    if istr[fd] == '+':
        #Output string is now all the letters before the addition sign and "tighten"
        ostr = istr[bk:fd] + ' tighten '
        #Updates the value of bk and fd to after the addition sign
        bk, fd = fd + 1, fd + 1
        #Keeps checking if the number goes on
        #The condition is while istr with the index of fd is an integer, it keeps going
        while fd < len(istr) and istr[fd].isdigit(): fd += 1
        #Updates output and the bk 
        ostr, bk = ostr + istr[bk:fd], fd
        #Prints out
        print(ostr)

    #Does the same thing but checks if its minus
    if fd < len(istr) and istr[fd] == '-':
        ostr = istr[bk:fd] + ' loosen '
        bk, fd = fd + 1, fd + 1
        while fd < len(istr) and istr[fd].isdigit(): fd += 1
        ostr, bk = ostr + istr[bk:fd], fd
        print(ostr)

    fd += 1