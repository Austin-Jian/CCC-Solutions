grid = [1, 2, 3, 4]
istr = input()
for i in range (len(istr)):
    if istr[i] == "H":
        grid = [grid[2], grid[3], grid[0], grid[1]]
    elif istr[i] == "V":
        grid = [grid[1], grid[0], grid[3], grid[2]]

print (grid[0], grid[1])
print (grid[2], grid[3])
