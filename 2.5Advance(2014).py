
import math
n = int (raw_input("enter n: "))
b = float(4.0/3.0)
c = float(22.0/7.0)
print b
value =0
for i in range(0,n):
    a = int(raw_input("Enter a: "))
    value = b*(math.pi*(math.pow(a,3)))
    print int(value)
    
    
#print value
