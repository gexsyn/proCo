import math
n = int (raw_input("enter n: "))
value =0
for i in range(0,n):
    a = float(raw_input("Enter a: "))
    value = 0.5 * math.ceil(2.0 * a)
    print float(value)

