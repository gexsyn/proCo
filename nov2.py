import random*
import sys
h = 3
l = 1
r = 1
while h > 7 or l> 7 or r > 7:

    user = raw_input("enter choice:")
    
    if user == "R":
        r += h
        if
        sys.stdout.write("\n"); sys.stdout.flush()
    if user == "L":
        l += h
        sys.stdout.write("\n"); sys.stdout.flush()
    comp = random.randint(0,1)# 0 is left and 1 is right
    if comp == 1:
        h+=r
        sys.stdout.write("\n"); sys.stdout.flush()
    if comp == 0:
        h+=l
        sys.stdout.write("\n"); sys.stdout.flush()

