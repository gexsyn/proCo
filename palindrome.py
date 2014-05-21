a = raw_input("Enter a word No spaces please:")

if a[::-1] == a and len(a)>0:
    print "yes"

else:
    print "no"
