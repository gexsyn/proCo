num = float(raw_input())

result = 0.0
for x in range(0,num):
    line = raw_input().split(" ")
    masterList.append(line)


for x in masterList:
    result = (x[0])/x[1]

print result
    
