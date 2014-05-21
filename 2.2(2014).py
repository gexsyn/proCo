num = int(raw_input())
finalD =0
n = 0
e = 90
s = 180
w = 270

masterList =[]

for x in range(0,num):
    line = raw_input().split(" ")
    masterList.append(line)


for x in masterList:
    x.sort()
    total =0
    if x[0] == 'N'and x[1] == 'N':
        total = abs(n-n)
    if x[0] == 'N'and x[1] == 'E':
        total = abs(n-e)
    if x[0] == 'N'and x[1] == 'S':
        total = abs(n-e)
    if x[0] == 'N'and x[1] == 'W':
        total = abs(n-e)
    if x[0] == 'N'and x[1] == 'E':
        total = abs(n-e)
    if x[0] == 'N'and x[1] == 'E':
        total = abs(n-e)
    if x[0] == 'N'and x[1] == 'E':
        total = abs(n-e)
    if x[0] == 'N'and x[1] == 'E':
        total = abs(n-e)
print total
        
        
            
            
            
            
    
