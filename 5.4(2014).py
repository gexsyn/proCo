num = int(raw_input())

    
masterList =[]

for x in range(0,num):
    line = raw_input().split(" ")
    masterList.append(line)


for x in masterList:
    x.sort()
    for i in x:
        i.rstrip()
    print i
    
        
        
        
        
        
        

                
                   
        



