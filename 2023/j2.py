n = int(input())
s = 0
for i in range (n):
    pep = input()
    if pep == "Poblano":
        s += 1500
    elif pep == "Mirasol":
        s += 6000
    elif pep == "Serrano":
        s += 15500
    elif pep == "Cayenne":
        s += 40000
    elif pep == "Thai":
        s += 75000
    elif pep == "Habanero":
        s += 125000

print (s)
