n = int(raw_input("enter:"))
z =[]
Mlist =[]
for x in range(0,n):
    a = raw_input("enter a:").split(" ")
    for y in a:
        z.append(y)
    a = raw_input("enter a:").split(" ")
    for y in a:
        z.append(y)
    a = raw_input("enter a:").split(" ")
    for y in a:
        z.append(y)

Mlist = sorted(z)

print Mlist
