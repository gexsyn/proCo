a = raw_input()
b = raw_input()
finalList =[]



for i in range(len(a)):
    number = str(int(a[i]) + int(b[i]))
    finalList.append(number[-1])

print finalList
    
    
    
    
