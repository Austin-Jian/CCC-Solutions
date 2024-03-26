og = input()
new = input()
funny = ''
silent = '-'

og_set = set(og)
new_set = set(new)

checked = set()
for char in new:
    if char not in checked:
        checked.add(char)
        if char not in og_set:
            funny = char
            break

bad = []
for char in og_set:
    if char not in new_set:
        bad.append(char)

test1 = ''
test2 = ''

for char in og:
    if char in new_set:
        test1 += char
        test2 += char
    else:
        if char == bad[0]:
            test1 += funny
        if char == bad[-1]:
            test2 += funny

if test1 == new:
    if bad[0] != bad[-1]:
        silent = bad[-1]
    print(bad[0], funny)
    print(silent)
elif test2 == new:
    if bad[0] != bad[-1]:
        silent = bad[0]
    print(bad[-1], funny)
    print(silent)
