n = int(raw_input(""))
for y in range(0,n):
    part = ""
    total = ""
    a = raw_input("")
    b = raw_input("")

    
    for x in b:
        part += x
    
        if part not in a:
            part = part[0:len(part)-1]
            

    finalPart = part
    
    if len(finalPart) == 0:
        print a+b

    else:
        SubA = a[:a.index(part)]
        z= b.index(finalPart)+len(finalPart)
        SubB = b[z:]
        total =  SubA + SubB
    
        print total
